#!/usr/bin/env python3
"""
reel_death_trigger.py

Monitorea las 'views' de un Reel de Instagram cada vez que se ejecuta
(pensado para correr vía cron cada 10-15 min) y calcula la pendiente
de crecimiento (views/minuto). Cuando la pendiente cae por debajo de
un umbral durante N lecturas consecutivas, considera que el reel
"murió", publica automáticamente el SIGUIENTE reel de una cola de
espera, y te avisa por Telegram.

Flujo de la cola:
- reel_queue.json contiene una lista de reels pendientes de publicar.
- Cuando el reel actual "muere": se saca el primero de la cola, se
  publica, y se convierte en el nuevo reel bajo supervisión. La cola
  se reduce en uno. El ciclo se repite indefinidamente.
- Si la cola se vacía, se te avisa por Telegram para que agregues más.

Nota matemática: comparar el ángulo de la curva contra arctan(2) es
matemáticamente equivalente a comparar la pendiente cruda contra
2 views/min, porque arctan es monótona creciente. Por eso el script
compara directamente la pendiente (más simple y sin dependencia de
la escala de un gráfico).

Requisitos:
- Cuenta de Instagram Business o Creator, vinculada a una Página de Facebook.
- App de Meta con permisos: instagram_business_basic,
  instagram_business_manage_insights, instagram_business_content_publish.
- Token de acceso (ya generado).
- Bot de Telegram (token + chat_id).
"""

import json
import os
import sys
import time
import requests
from datetime import datetime, timezone

# ============ CONFIG ============
GRAPH_API_VERSION = "v22.0"
GRAPH_API_BASE = "https://graph.instagram.com"  # API de Instagram con login directo

ACCESS_TOKEN = os.environ.get("IG_ACCESS_TOKEN", "TU_TOKEN_AQUI")
IG_USER_ID = os.environ.get("IG_USER_ID", "TU_IG_USER_ID_AQUI")

# ID del reel inicial a monitorear. Una vez que el sistema empiece a
# rotar reels automáticamente, este valor ya no se usa (se guarda el
# ID actual en STATE_FILE).
INITIAL_REEL_MEDIA_ID = os.environ.get("REEL_MEDIA_ID", "ID_DEL_REEL_A_MONITOREAR")

# Umbral: pendiente en views/minuto. (equivalente a arctan(2))
SLOPE_THRESHOLD = 2.0

# Cuántas lecturas consecutivas bajo el umbral se requieren antes de
# disparar la publicación (para evitar falsos positivos por ruido).
CONSECUTIVE_READINGS_REQUIRED = 3

# Tolerancia Adaptativa por Mérito: si en cualquier momento de su vida
# el reel registra una sola lectura con una pendiente por encima de
# este umbral de mérito, se le regala un período de "congelamiento" de
# las decisiones (MERIT_GRACE_HOURS). Durante ese tiempo las vistas se
# siguen leyendo y guardando con normalidad, pero el contador de rachas
# de bajo rendimiento NO se toca -- ni suma, ni resetea, simplemente se
# ignora para las decisiones. Pasado ese tiempo, las rachas se
# reintegran a las decisiones con normalidad. Si el reel vuelve a
# demostrar una racha alta durante ese congelamiento, el temporizador
# se reinicia a 24h de nuevo desde ese momento.
MERIT_GRACE_TRIGGER_SLOPE = 5.0  # views/min
MERIT_GRACE_HOURS = 24
MERIT_GRACE_SECONDS = MERIT_GRACE_HOURS * 3600

# Período de gracia: durante las primeras N horas después de publicado,
# el reel NUNCA se considera "muerto", sin importar qué tan baja esté
# la pendiente. Esto evita matar reels que arrancan lento pero luego
# despegan (el algoritmo de distribución de Instagram suele tardar en
# "probar" el contenido antes de empujarlo con fuerza).
GRACE_PERIOD_HOURS = 3
GRACE_PERIOD_SECONDS = GRACE_PERIOD_HOURS * 3600

# Archivos de estado persistente
STATE_FILE = "reel_state.json"
QUEUE_FILE = "reel_queue.json"

# --- Telegram ---
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "TU_TELEGRAM_BOT_TOKEN_AQUI")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "TU_TELEGRAM_CHAT_ID_AQUI")
# =================================


# ---------- Estado y cola ----------

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
            # Compatibilidad: si el archivo es de antes de agregar el
            # período de gracia, asumimos que "ya pasó" el período de
            # gracia (resta 1 hora extra al tiempo actual como margen),
            # para no reiniciar el reloj de reels que ya llevaban rato.
            if "published_at" not in state:
                state["published_at"] = datetime.now(timezone.utc).timestamp() - GRACE_PERIOD_SECONDS
            if "peak_slope" not in state:
                state["peak_slope"] = 0.0
            if "merit_grace_until" not in state:
                state["merit_grace_until"] = 0
            return state
    return {
        "current_reel_id": INITIAL_REEL_MEDIA_ID,
        "readings": [],
        "below_threshold_streak": 0,
        "peak_slope": 0.0,
        "merit_grace_until": 0,
        # No sabemos la hora real de publicación del reel inicial (el
        # que configuraste a mano), así que asumimos "ahora mismo" por
        # seguridad -- esto le da el período de gracia completo antes
        # de poder matarlo. Si ya llevaba horas publicado, edita este
        # valor a mano en reel_state.json restándole las horas reales.
        "published_at": datetime.now(timezone.utc).timestamp(),
    }


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def load_queue():
    """La cola es una lista de objetos: [{"video_url": "...", "caption": "..."}]"""
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_queue(queue):
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2, ensure_ascii=False)


# ---------- Telegram ----------

def send_telegram_message(text):
    if TELEGRAM_BOT_TOKEN.startswith("TU_") or TELEGRAM_CHAT_ID.startswith("TU_"):
        print("[WARN] Telegram no configurado, se omite notificación.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(
            url,
            data={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"},
            timeout=15,
        )
    except Exception as e:
        print(f"[WARN] No se pudo enviar notificación de Telegram: {e}")


# ---------- Instagram API ----------

def get_reel_views(media_id, token):
    url = f"{GRAPH_API_BASE}/{media_id}/insights"
    params = {"metric": "views", "access_token": token}
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    try:
        return data["data"][0]["values"][0]["value"]
    except (KeyError, IndexError):
        raise RuntimeError(f"Respuesta inesperada de la API: {data}")


def compute_slope(prev_reading, curr_reading):
    """Pendiente en views/minuto entre dos lecturas."""
    dt_minutes = (curr_reading["ts"] - prev_reading["ts"]) / 60.0
    if dt_minutes <= 0:
        return None
    dv = curr_reading["views"] - prev_reading["views"]
    return dv / dt_minutes


def _raise_with_instagram_message(resp):
    """Si la respuesta de Instagram trae un mensaje de error explicando
    la causa (ej. caption muy largo, video inválido), lo mostramos en
    vez del genérico '400 Bad Request'."""
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        try:
            detail = resp.json().get("error", {}).get("message", "")
        except Exception:
            detail = ""
        if detail:
            raise RuntimeError(f"{e} -- Motivo de Instagram: {detail}") from None
        raise


def create_media_container(ig_user_id, token, video_url, caption):
    url = f"{GRAPH_API_BASE}/{ig_user_id}/media"
    params = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": caption,
        "access_token": token,
    }
    resp = requests.post(url, params=params, timeout=30)
    _raise_with_instagram_message(resp)
    return resp.json()["id"]


def wait_for_container_ready(container_id, token, timeout_s=180, poll_s=5):
    url = f"{GRAPH_API_BASE}/{container_id}"
    elapsed = 0
    while elapsed < timeout_s:
        resp = requests.get(
            url, params={"fields": "status_code", "access_token": token}, timeout=15
        )
        resp.raise_for_status()
        status = resp.json().get("status_code")
        if status == "FINISHED":
            return True
        if status == "ERROR":
            raise RuntimeError("El contenedor de medios falló al procesarse.")
        time.sleep(poll_s)
        elapsed += poll_s
    raise TimeoutError("Timeout esperando que el contenedor esté listo.")


def publish_container(ig_user_id, container_id, token):
    url = f"{GRAPH_API_BASE}/{ig_user_id}/media_publish"
    params = {"creation_id": container_id, "access_token": token}
    resp = requests.post(url, params=params, timeout=30)
    _raise_with_instagram_message(resp)
    return resp.json()  # {"id": "<nuevo_media_id>"}


CAPTION_MAX_LENGTH = 2200


def publish_next_from_queue():
    """Publica el primer reel de la cola. Devuelve el nuevo media_id, o None si la cola está vacía."""
    queue = load_queue()

    if not queue:
        print("[QUEUE] La cola está vacía.")
        send_telegram_message(
            "⚠️ <b>Cola de reels vacía</b>\n"
            "El reel actual murió pero no hay más contenido en espera. "
            "Agrega reels a reel_queue.json para que la automatización siga."
        )
        return None

    next_item = queue[0]
    caption = next_item.get("caption", "")

    if len(caption) > CAPTION_MAX_LENGTH:
        print(f"[ERROR] El caption del siguiente reel tiene {len(caption)} caracteres "
              f"(máximo {CAPTION_MAX_LENGTH}). No se publica, se deja en la cola.")
        send_telegram_message(
            "⚠️ <b>Caption demasiado largo</b>\n"
            f"El siguiente reel en la cola tiene {len(caption)} caracteres "
            f"(el límite de Instagram es {CAPTION_MAX_LENGTH}).\n"
            "No se publicó. Acórtalo en reel_queue.json y el sistema lo "
            "reintentará en la próxima ejecución."
        )
        return None

    queue.pop(0)  # saca el primero (FIFO), ya validado
    print(f"[ACTION] Publicando siguiente reel: {next_item.get('caption', '')[:50]}...")

    container_id = create_media_container(
        IG_USER_ID, ACCESS_TOKEN, next_item["video_url"], next_item.get("caption", "")
    )
    wait_for_container_ready(container_id, ACCESS_TOKEN)
    result = publish_container(IG_USER_ID, container_id, ACCESS_TOKEN)
    new_media_id = result.get("id")

    # Solo guardamos la cola actualizada si TODO salió bien
    save_queue(queue)

    print(f"[ACTION] Publicado. Nuevo reel ID: {new_media_id}")
    send_telegram_message(
        "✅ <b>Reel publicado automáticamente</b>\n"
        f"El reel anterior había 'muerto' (crecimiento &lt; {SLOPE_THRESHOLD} views/min).\n"
        f"Nuevo reel en supervisión: <code>{new_media_id}</code>\n"
        f"Quedan {len(queue)} reel(s) en espera."
    )
    return new_media_id


# ---------- Lógica principal ----------

def main():
    if ACCESS_TOKEN.startswith("TU_") or IG_USER_ID.startswith("TU_"):
        print("ERROR: configura ACCESS_TOKEN / IG_USER_ID "
              "(vía variables de entorno o editando el script).")
        sys.exit(1)

    state = load_state()
    current_reel_id = state["current_reel_id"]

    if current_reel_id.startswith("ID_DEL_REEL"):
        print("ERROR: configura REEL_MEDIA_ID inicial.")
        sys.exit(1)

    try:
        views = get_reel_views(current_reel_id, ACCESS_TOKEN)
    except Exception as e:
        print(f"[ERROR] No se pudo obtener views del reel {current_reel_id}: {e}")
        send_telegram_message(
            f"❌ <b>Error al leer las vistas del reel</b>\n"
            f"Reel: <code>{current_reel_id}</code>\n"
            f"Motivo: {e}\n"
            f"El monitoreo se reintentará en la próxima ejecución."
        )
        return

    now_ts = datetime.now(timezone.utc).timestamp()
    reading = {"ts": now_ts, "views": views}
    state["readings"].append(reading)

    print(f"[{datetime.now(timezone.utc).isoformat()}] reel={current_reel_id} views={views}")

    if len(state["readings"]) < 2:
        save_state(state)
        print("Primera lectura registrada, esperando la siguiente para calcular pendiente.")
        return

    prev = state["readings"][-2]
    slope = compute_slope(prev, reading)

    if slope is None:
        save_state(state)
        return

    print(f"Pendiente actual: {slope:.3f} views/min (umbral: {SLOPE_THRESHOLD})")

    # Actualizamos el pico de velocidad de este reel (para la
    # Tolerancia Adaptativa por Mérito), sin importar si estamos en
    # período de gracia o no -- un reel puede volar justo al principio.
    state["peak_slope"] = max(state.get("peak_slope", 0.0), slope)

    # Período de gracia: no evaluamos "muerte" mientras el reel sea
    # muy nuevo, para no matarlo por un arranque lento normal.
    elapsed_since_publish = now_ts - state.get("published_at", now_ts)
    if elapsed_since_publish < GRACE_PERIOD_SECONDS:
        remaining_min = (GRACE_PERIOD_SECONDS - elapsed_since_publish) / 60
        print(f"[GRACIA] El reel lleva {elapsed_since_publish/3600:.2f}h publicado, "
              f"todavía dentro del período de gracia de {GRACE_PERIOD_HOURS}h "
              f"(faltan {remaining_min:.0f} min). No se evalúa 'muerte' todavía.")
        save_state(state)
        return

    # Tolerancia Adaptativa por Mérito: si esta lectura demuestra un
    # rendimiento excepcional, (re)armamos el congelamiento de 24h.
    if slope > MERIT_GRACE_TRIGGER_SLOPE:
        state["merit_grace_until"] = now_ts + MERIT_GRACE_SECONDS
        print(f"[MÉRITO] Pendiente de {slope:.2f} views/min superó el umbral de mérito "
              f"({MERIT_GRACE_TRIGGER_SLOPE}). Congelando decisiones por {MERIT_GRACE_HOURS}h.")

    merit_grace_until = state.get("merit_grace_until", 0)
    if now_ts < merit_grace_until:
        remaining_h = (merit_grace_until - now_ts) / 3600
        print(f"[MÉRITO] Decisiones congeladas por buen rendimiento reciente "
              f"(faltan {remaining_h:.1f}h). El contador de rachas no se toca.")
        save_state(state)
        return

    if slope < SLOPE_THRESHOLD:
        state["below_threshold_streak"] += 1
    else:
        state["below_threshold_streak"] = 0

    print(f"Lecturas consecutivas bajo el umbral: "
          f"{state['below_threshold_streak']}/{CONSECUTIVE_READINGS_REQUIRED}")

    if state["below_threshold_streak"] >= CONSECUTIVE_READINGS_REQUIRED:
        print("El reel se considera 'muerto'. Publicando el siguiente de la cola.")
        try:
            new_reel_id = publish_next_from_queue()
            if new_reel_id:
                # Reiniciamos el monitoreo sobre el nuevo reel
                state = {
                    "current_reel_id": new_reel_id,
                    "readings": [],
                    "below_threshold_streak": 0,
                    "peak_slope": 0.0,
                    "merit_grace_until": 0,
                    "published_at": now_ts,
                }
            else:
                # Cola vacía: seguimos "vigilando" el mismo reel muerto
                # para no perder el hilo, pero sin volver a disparar
                # publicaciones hasta que agregues contenido a la cola.
                state["below_threshold_streak"] = 0
        except Exception as e:
            print(f"[ERROR] Falló la publicación: {e}")
            send_telegram_message(f"❌ <b>Error al publicar el siguiente reel</b>\n{e}")

    save_state(state)


if __name__ == "__main__":
    main()
