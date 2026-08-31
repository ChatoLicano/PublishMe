


**¿COMO INSTALAR PUBLISH ME?**


## ⚠️ Cosas que necesitas (pre-requisitos) para instalar Publish Me 

- Una cuenta de **Instagram Business o Creator**, vinculada a una **Página de
  Facebook**.
- Una cuenta de **GitHub** (gratis).
- Una cuenta de **Cloudinary** (gratis) para alojar tus videos con un link
  público.
- Una cuenta de **Telegram** (para recibir notificaciones).
- Una cuenta de **cron-job.org** (gratis) para disparar el sistema cada
  15 minutos con precisión.
- Media hora a una hora de tu tiempo, sin prisa, la primera vez.




















## Instalación paso a paso


### 1. Usa esta plantilla de GitHub
Dale click a este link "https://github.com/ChatoLicano/PublishMe" → luego dale click al boton verde que dice **"Use this template"**
(no "Fork") → elige un nombre para tu copia → márcalo como **Privado**.
Esto te crea una copia 100% tuya e independiente, sin conexión al original.


### 2. Crea tu propia app en Meta for Developers
1. Convierte tu cuenta de Instagram a **Business o Creator**
   (Instagram → Configuración → Cuenta → Cambiar a cuenta profesional).
2. Vincúlala a una **Página de Facebook** (créala gratis si no tienes una).
3. Ve a [developers.facebook.com](https://developers.facebook.com) → **Mis
   apps** → **Crear app** → tipo "Business".
4. En "Casos de uso", filtra por **"Administración de contenido"** y elige
   **"Administrar mensajes y contenido en Instagram"**.
5. Dentro de "Personalizar caso de uso" → "Configuración de la API con
   inicio de sesión" → agrega los permisos:
   `instagram_business_basic`, `instagram_business_manage_insights`,
   `instagram_business_content_publish`.


### 3. Agrégate como tu propio "Instagram tester"
1. En el panel de tu app → **Roles de la app** → **Roles** → **Agregar
   personas** → selecciona **"Evaluador de Instagram"** → escribe tu propio
   usuario de Instagram.
2. Abre Instagram en tu celular con esa cuenta → **Configuración → Cuentas
   centralizadas / Aplicaciones y sitios web** → acepta la invitación
   pendiente.
> ⚠️ **Error común:** si te salta "Rol de desarrollador insuficiente" al
> generar el token, es porque falta este paso. Complétalo antes de seguir.


### 4. Genera tu token de acceso
En "Configuración de la API con inicio de sesión" → sección "Generar tokens
de acceso" → agrega tu cuenta → autoriza los 4 permisos (perfil, comentarios,
mensajes, **contenido y publicarlo**, **insights**) → copia el token.

Guárdalo en un lugar seguro. Lo vas a necesitar en el paso 6.

### 5. Consigue tu `IG_USER_ID` y el `REEL_MEDIA_ID` inicial

En [Graph API Explorer](https://developers.facebook.com/tools/explorer):

- `me/accounts` → obtén el ID de tu Página.
- `{ID_PAGINA}?fields=instagram_business_account` → ese número es tu
  `IG_USER_ID`.
- `me/media` (usando tu token, dominio `graph.instagram.com`) → lista tus
  reels recientes, copia el `id` del que quieras monitorear primero.

### 6. Configura los 5 Secrets en GitHub

En tu repositorio → **Settings → Secrets and variables → Actions → New
repository secret**. Crea estos 5, uno por uno:

| Nombre | Valor |
|---|---|
| `IG_ACCESS_TOKEN` | El token del paso 4 |
| `IG_USER_ID` | El número del paso 5 |
| `REEL_MEDIA_ID` | El ID del reel inicial del paso 5 |
| `TELEGRAM_BOT_TOKEN` | Ver paso 8 |
| `TELEGRAM_CHAT_ID` | Ver paso 8 |

### 7. Activa permisos de escritura para Actions

**Settings → Actions → General → Workflow permissions** → selecciona
**"Read and write permissions"** → Save. Sin esto, el sistema no puede
guardar su propio progreso.

### 8. Crea tu bot de Telegram

1. Habla con **@BotFather** en Telegram → `/newbot` → sigue las
   instrucciones → copia el token que te da.
2. Envíale cualquier mensaje a tu bot nuevo.
3. Visita `https://api.telegram.org/bot<TU_TOKEN>/getUpdates` → busca
   `"chat":{"id":...}` → ese número es tu `TELEGRAM_CHAT_ID`.

### 9. Configura Cloudinary (para alojar tus videos)

Crea una cuenta gratis en [cloudinary.com](https://cloudinary.com). Cada vez
que subas un video, copia su link de **"Incrustar"**
(`player.cloudinary.com/embed/?cloud_name=...&public_id=...`) — el sistema
lo convierte automáticamente al link directo que Instagram necesita.

### 10. Configura el disparador externo (cron-job.org)

> ⚠️ **Importante:** el "cron" interno de GitHub Actions (`schedule:`) es
> poco confiable en repos privados/gratuitos — puede atrasarse horas sin
> avisar. Por eso usamos un disparador externo.

1. Crea un token en
   [github.com/settings/tokens?type=beta](https://github.com/settings/tokens?type=beta)
   con acceso solo a tu repositorio y permiso **Actions: Read and write**.
2. Crea una cuenta gratis en [cron-job.org](https://cron-job.org).
3. Crea un cronjob nuevo:
   - **URL**: `https://api.github.com/repos/TU_USUARIO/TU_REPO/actions/workflows/monitor.yml/dispatches`
   - **Método**: `POST`
   - **Horario**: cada 15 minutos
   - **Headers**: `Authorization: Bearer TU_TOKEN` y
     `Accept: application/vnd.github+json`
   - **Body**: `{"ref":"main"}`

### 11. Agrega tu primer reel a la cola de espera

Edita `reel_queue.json` en GitHub, pega tu `video_url` (link de Incrustar de
Cloudinary) y tu `caption` (con saltos de línea normales, sin preocuparte del
formato) → Commit. Un workflow automático (`fix_queue.yml`) lo arregla solo
en segundos.

> ⚠️ El caption no puede superar **2200 caracteres** (límite de Instagram).
> El sistema te avisa por Telegram si te pasas, sin gastar el intento.

---

## Ajusta Pulso a tu estilo de creador

Todos estos valores viven al inicio de `reel_death_trigger.py`:

```python
SLOPE_THRESHOLD = 2.0          # views/min mínimo antes de sospechar
CONSECUTIVE_READINGS_REQUIRED = 3   # rachas malas seguidas para confirmar
GRACE_PERIOD_HOURS = 3         # horas de gracia al nacer un reel
MERIT_GRACE_TRIGGER_SLOPE = 5.0     # views/min que activan la tolerancia por mérito
MERIT_GRACE_HOURS = 24         # horas de congelamiento que gana un reel excepcional
```

No hay valores "correctos" universales — experimenta con los tuyos.

---

## Solución de problemas comunes

**"Rol de desarrollador insuficiente" al generar el token**
→ Falta agregarte como Instagram tester (paso 3) y aceptar la invitación
desde el celular.

**El archivo `reel_queue.json` da error de JSON al correr el script**
→ Probablemente pegaste texto con saltos de línea "crudos". Espera a que
corra `fix_queue.yml` automáticamente (unos segundos después del commit), o
corre `fix_reel_queue.py` manualmente.

**El sistema no publica aunque el reel claramente ya murió**
→ Revisa el `reel_state.json`: compara el `ts` de la última lectura contra
la hora actual. Si el intervalo es mucho mayor a 15 min, revisa que
cron-job.org esté activo y que el token no haya expirado.

**Error "400 Bad Request" al publicar**
→ Con la versión actual del script, el mensaje de Telegram te dice el motivo
real (caption muy largo, video no descargable, etc.), no solo el código.

---

## Aviso importante

Cada instancia de Pulso opera bajo la responsabilidad de quien la instala:
tus credenciales, tu app de Meta, tu cumplimiento de las políticas de
Meta/Instagram. Pulso no almacena ni tiene acceso a los datos de nadie más
que de quien lo instala en su propio repositorio.

Ojo <o> : Cada creador monta su propia instancia, con sus propios tokens y su propia app de Meta.
Lo que quiere decir que Publih Me usara tus crdenciales pero estaran encriptadas a los "ojos" de PublishMe (todo vive en tu cuenta de GitHub, y ningun otro a excepcion tuya tiene control a tu informacion).
