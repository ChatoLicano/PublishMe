#!/usr/bin/env python3
"""
fix_reel_queue.py

Repara automáticamente reel_queue.json cuando lo editaste directamente
a mano (pegando el video_url y el caption con saltos de línea "normales",
como los copias de cualquier lado) y eso rompió el formato JSON.

Convierte los saltos de línea "crudos" que queden DENTRO de un texto
entre comillas en el código \\n que JSON necesita, sin que tengas que
hacerlo tú a mano.

USO:
    Después de editar reel_queue.json pegando el video_url (link de
    "Incrustar" de Cloudinary o link directo, cualquiera de los dos)
    y el caption con saltos de línea normales, simplemente ejecuta:

        python fix_reel_queue.py

    El archivo se corrige en el mismo lugar (in-place): arregla el
    formato JSON y convierte automáticamente cualquier link de
    "Incrustar" de Cloudinary al link directo .mp4 que necesita
    Instagram. Queda listo para que reel_death_trigger.py lo use.

LIMITACIÓN IMPORTANTE:
    No uses comillas rectas dobles ( " ) sueltas dentro del caption,
    porque el sistema las usa para saber dónde empieza y termina cada
    texto. Si necesitas comillas dentro del caption, usa las curvas
    ( “ y ” ) en su lugar — esas sí funcionan sin problema.
"""

import json
import os
import sys
from urllib.parse import urlparse, parse_qs

QUEUE_FILE = "reel_queue.json"


def resolve_video_url(url: str) -> str:
    """
    Si el link es un link de 'Incrustar' de Cloudinary
    (player.cloudinary.com/embed/?cloud_name=X&public_id=Y), lo convierte
    automáticamente al link directo del archivo .mp4. Si ya es un link
    directo (o de cualquier otro tipo), lo deja tal cual.
    """
    parsed = urlparse(url)

    if "player.cloudinary.com" in parsed.netloc:
        params = parse_qs(parsed.query)
        cloud_name = params.get("cloud_name", [None])[0]
        public_id = params.get("public_id", [None])[0]

        if cloud_name and public_id:
            direct_url = f"https://res.cloudinary.com/{cloud_name}/video/upload/{public_id}.mp4"
            print(f"[INFO] Link de Incrustar detectado en '{url[:50]}...', "
                  f"convertido a: {direct_url}")
            return direct_url
        else:
            print(f"[WARN] No pude leer cloud_name/public_id del link '{url[:50]}...', "
                  "se dejará tal cual (puede que no funcione).")

    return url


def sanitize_json_text(raw: str) -> str:
    """
    Recorre el texto crudo del archivo y, solo cuando está DENTRO de un
    valor de texto entre comillas, convierte los saltos de línea reales
    en la secuencia \\n que el formato JSON requiere.
    """
    result = []
    in_string = False
    escape = False

    for ch in raw:
        if in_string:
            if escape:
                result.append(ch)
                escape = False
                continue
            if ch == "\\":
                result.append(ch)
                escape = True
                continue
            if ch == '"':
                in_string = False
                result.append(ch)
                continue
            if ch == "\n":
                result.append("\\n")
                continue
            if ch == "\r":
                continue  # se descarta, \n ya cubre el salto de línea
            if ch == "\t":
                result.append("\\t")
                continue
            result.append(ch)
        else:
            if ch == '"':
                in_string = True
            result.append(ch)

    return "".join(result)


def main():
    if not os.path.exists(QUEUE_FILE):
        print(f"ERROR: no encontré '{QUEUE_FILE}' en esta carpeta.")
        sys.exit(1)

    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        raw = f.read()

    # Si ya es válido, solo revisamos si hay links de Incrustar que convertir
    try:
        data = json.loads(raw)
        changed = False
        for item in data:
            if "video_url" in item:
                new_url = resolve_video_url(item["video_url"])
                if new_url != item["video_url"]:
                    item["video_url"] = new_url
                    changed = True

        if changed:
            with open(QUEUE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✅ Archivo ya era JSON válido. Se convirtieron links de Incrustar. "
                  f"({len(data)} reel(s) en la cola)")
        else:
            print("✅ El archivo ya estaba en formato JSON válido, no se hicieron cambios.")
            print(f"   ({len(data)} reel(s) en la cola)")
        return
    except json.JSONDecodeError:
        pass  # seguimos, intentamos repararlo

    fixed_raw = sanitize_json_text(raw)

    try:
        data = json.loads(fixed_raw)
    except json.JSONDecodeError as e:
        print("❌ No pude reparar el archivo automáticamente.")
        print(f"   Error: {e}")
        print("   Revisa si hay comillas rectas ( \" ) sueltas dentro de algún")
        print("   caption -- cámbialas por comillas curvas ( \u201c \u201d ) y vuelve a intentar.")
        sys.exit(1)

    # Convierte automáticamente cualquier link de "Incrustar" de Cloudinary
    # al link directo .mp4 que necesita Instagram, y avisa si algún
    # caption excede el límite de 2200 caracteres de Instagram.
    CAPTION_MAX_LENGTH = 2200
    for i, item in enumerate(data, start=1):
        if "video_url" in item:
            item["video_url"] = resolve_video_url(item["video_url"])
        caption_len = len(item.get("caption", ""))
        if caption_len > CAPTION_MAX_LENGTH:
            print(f"⚠️  AVISO: el reel #{i} de la cola tiene un caption de "
                  f"{caption_len} caracteres (el límite de Instagram es "
                  f"{CAPTION_MAX_LENGTH}). Acórtalo o Instagram lo rechazará "
                  f"al intentar publicarlo.")

    # Reescribimos el archivo ya en formato JSON válido y bien indentado
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Archivo reparado correctamente. {len(data)} reel(s) en la cola.")


if __name__ == "__main__":
    main()
