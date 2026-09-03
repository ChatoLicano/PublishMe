  

### ¿COMO INSTALAR PUBLISH ME?

**RESUMEN DE ACCIONES QUE EJECUTAREMOS EN LA INSTALACIÓN PASO A PASO**
1. Una cuenta de Instagram Business o Creator , vinculada a una página de Facebook .
2. Una cuenta de GitHub (gratis).
3. Una cuenta de Cloudinary (gratis) para alojar tus vídeos con un enlace público.
4. Una cuenta de Telegram (para recibir notificaciones).
5. Una cuenta de cron-job.org (gratis) para disparar el sistema cada 15 minutos con precisión.
6. Media hora a una hora de tu tiempo, sin prisa, la primera vez.
****
### INSTALACION PASO A PASO

**1. USA ESTA **PLANTILLA** DE GITHUB**
1. Dale clic a este enlace " https://github.com/ChatoLicano/PublishMe "
2. Luego dale clic al botón verde que dice "Usar esta plantilla"
3. Luego dale a la opción Crear un nuevo repositorio → Selecciona Nombre del repositorio y escríbele en el espacio un nombre a tu copia de PublishMe → Ve a Configuración → Elige visibilidad
4. Cambia de "Público" a "Privado" Esto crea una copia 100% tuya e independiente de PublishMe.
Listo ya tienes una copia oficial de PublishMe, dentro de tu ordenador
****
**2. Configurar tu Instagram como Empresa**
1. En la cuenta de instagram donde quieres usar PublishMe, entra (entra por celular)
2. En la parte de abajo donde esta el "Feed", "Reel", "Mensajes Directos", "Explorar" y "Perfil", dale a "Perfil"
3. Dale a las Tres Rayitas (Configuración) en la parte superior derecha
4. Busca en configuraciones y selecciona "Tipo de cuenta y herramientas"
5. Selecciona "Tipo de Cuenta"
6. Busca "Cambiar tipo de cuenta" (esta en letra pequeña y azul)
7. Selecciona "Cambiar a cuenta de empresa"
Listo, ahora ya tenemos tu cuenta de instagram como empresa
****
**3. Crear una Fan Page (Pagina de Facebook)**
1. Entra en Facebook
2. Selecciona el Menú de Facebook (de icono ⌘)
3. Dale haga clic en "Páginas"
4. Dale a "+ Crear página"
5. Dale a "Pagina Publica"
6. Dale a "Empezar"
7. Ponle un Nombre y escribe una categoría (cualquiera categoría, el tipo de categoría no interesa por ahora)
8. Dale a "Crear Página"
9. Dale full a Siguiente y Omitir y al final dale
Listo ahora ya tenemos la Página de Facebook
****
**4. Vincular tu Instagram configurado como Empresa y la Fan Page**
1. Entra en Facebook
2. Dale click a Perfil que se encuentra en la parte superior derecha
3. Selecciona la Página de Facebook
4. Dale a "Configuración" que se encuentra al lado izquierdo
5. En Configuración y privacidad busca "Cuentas vinculadas"
6. Selecciona "Instagram No conectado"
7. Haz clic en "Conectar cuenta"
8. Haz clic en "Conectar"
9. Haz click en "Continuar"
10. Entra con la cuenta de instagram en la que vas a usar PublishMe
11. Dale "Agregar"
12. Dale a la "X" (cierrala) Ahora ya tienes conectado tu instagram donde vas a usar PublishMe y la página de facebook que hemos creado más antes"
Listo, ahora ya tenemos vinculado tu Instagram donde vas a usar publishme con la Fan Page, esto nos va a permitir crear una app en meta for developers para asi obtener los permisos necesarios para que el sistema pueda arrancar

**5. Crea tu propia app en Meta for Developers**
1. Ve a [developers.facebook.com](https://developers.facebook.com) y entra con tu cuenta de Facebook.
2. Arriba a la derecha, dale clic a "Mis apps".
3. Dale clic a "Crear app".
4. En "Detalles de la app", escribe un nombre (anota el nombre algun lado, porque lo vamos a utilizar en el paso "8. Consigue tu IG_USER_ID") y tu correo de contacto → dale "Siguiente".
5. En "Casos de uso", en el menú de la izquierda "Filtrar por", dale clic a "Administración de contenido".
6. De la lista que aparece a la derecha, marca la casilla de "Administrar mensajes y contenido en Instagram" → dale "Siguiente".
7. En "Negocio", selecciona la cuenta de Instagram donde donde quieres usar PublishMe
8. En "Requisitos" dale a "Siguiente"
9. En "Resumen", revisa que todo esté bien → dale "Crear app" (puede pedirte confirmar tu contraseña de Facebook).
Listo, ahora esto nos va a permitir agregar los 5 permisos necesarios para que el sistema arranque

**6. Agrega los permisos necesarios**
1. En el panel de tu app, busca en el menú izquierdo "Casos de uso" (al ícono de lápiz ✏️) → y dale click
2. Dale click a "Personalizar".
3. Busca un boton azul "Add all required permissions" → y dale click
4. Ahora busca en la parte izquierda algo que diga "Permisos y funciones" → y dale click
5. Busca en la lista "instagram_business_manage_insights" y dale clcik al "+ Agregar" que esta alado suyo
6. Busca en la lista "instagram_business_content_publish" y dale clcik al "+ Agregar" que esta alado suyo
Listo, con esto ya tenemos los 5 permisos habilitados para que el sistema arranque

**7. Agrégate como tu propio "Instagram tester"**
1. Dale clic a "Roles de la app" (esta en el lado izquierdo, entre los iconos de Rueda y Campana)
2. Dale clck a "Roles".
3 Dale clic al botón azul "Agregar personas".
4. En la ventana que se abre, marca la casilla marca "Evaluador de Instagram" (NO el "Evaluador" sino "Evaluador de Instagram")
6. En el campo de búsqueda de abajo → escribe el nombre de usuario de la cuenta de Instagram donde quieres usar PublishMe (el mismo que configuraste como Empresa en el paso 2) → luego te aparecerá tu cuenta de instagram → hazle click a tu cuenta de instagram.
7. Dale clic a "Agregar".
8. Ahora entra a https://www.instagram.com/ e inicia sesion con la misma cuenta de instagram.
9. Dale a las "tres rayitas" → "Configuración" → busca y entra a "Permisos del sitio web"
10. Dale a "Aplicaciones y sitios web"
11. Dale a "Invitaciones para evaluadores"
12. Y te aparecerá unos párrafos de texto (si quieres lo lees) → y luego de leerlo dale a "Aceptar"
Listo, ahora con este paso, ya no te a aparecerá el error de "Rol de desarrollador insuficiente" cuando vayamos a generar el token

**8. Genera tu token de acceso**
1. Vuelve a darle a "Casos de uso" → "Personalizar"
2. Baja hasta la sección "2. Generar tokens de acceso" → y dale a "Agregar cuenta" → y luego dale a "Continuar" en el aviso que aparece
3. Se abre una ventana de Instagram: Inicia sesion con la cuenta de instagram donde quieres usar PublishMe
4. Te va a aparecer una pantalla pidiendo permisos — dale "Permitir".
5. Luego dale al texto en azul que dice "Generar token"
6. Inicia sesion nuavemente con la cuenta de instagram donde quieres usar PublishMe
7. Te va a aparecer una nueva pantalla con otros permisos (si quieres lo lees) → y luego le das a "Permitir"
8. Te va aparecerá una tarjeta
9. Dale click a la casilla alado de "Entendido"
10. Dale al boton "Copiar"
11. Abre un bloc de notas y pega eso que copiaste
12. Listo, acabas de obtener EL TOKEN DE ACCESO. Guarda el bloc de notas y no lo compartas con nadie
Ahora ya tienes el TOKEN DE ACCESO que es la 1ra variable de las 5 variables que necesita el sistema para funcionar

**9. Consigue tu IG_USER_ID**
1. Ve a [developers.facebook.com](https://developers.facebook.com) y entra con tu cuenta de Facebook.
2. Arriba a la derecha, dale clic a "Mis apps".
3. Selecciona la app que hemos creado
4. Dale a "Casos de uso" → y luego "Personalizar"
5. Baja hasta la sección "2. Generar tokens de acceso"
6. En "Cuenta de Instagram" fijate que hay un numero largo de 17 numeros, cópialo y pégalo a un bloc de notas
7. Listo, acbas de obtener tu IG_USER_ID
Listo, ahora ya tenenos el IG_USER_ID, que es la 2da variable de las 5 variables que necesita el sistema para funcionar 

**10. Consigue tu REEL_MEDIA_ID**
1. Haz click a este enlace [Graph API Explorer](https://developers.facebook.com/tools/explorer)
2. En "App de Meta" (panel derecho - en letras chiquitas) → elige la App que Creaste (en el paso 5. **Crea tu propia app en Meta for Developers**)
3. Selecciona el nombre de tu app
4. En el campo "Token de acceso", pega el TOKEN DE ACCESO que copiamos en el bloc de notas (paso 8. **Genera tu token de acceso**)
5. En la barra de consulta (donde dice algo como "me?fields=id,name"), bórrala y escribe: "me/media" → dale clic en "Enviar". (Si te da un error, revisa que el dominio a la izquierda de la barra diga .instagram.com, no .facebook.com — cámbialo con el desplegable si hace falta.)
6. Te va a devolver una lista de tus publicaciones recientes con sus IDs
7. Copia el primer ID el que se encuentra mas arriba → y pégalo en un bloc de notas
Listo, ahora ya tienes el REEL_MEDIA_ID, que es la 3ra variable de las 5 variables que necesita el sistema para funcionar

**11. Crea tu bot de Telegram que te notificara de todo lo que le ocurra al sistema y genera el TELEGRAM_BOT_TOKEN**
1. Instala Telegram y crea una cuenta o inicia sesion
2. Dale a la "lupa"
3. Y escribe "botfather"
4. Selecciona una cuenta que diga "BotFather y con una icono de cuenta verificada" (BotFather es una cuenta verificada por telegram) → dale clic
5. Escribe "/start" luego te respondera → y tu escrbiras "/newbot"
6. Luego te dira "Bien. Ahora elijamos un nombre de usuario para tu bot. Debe terminar en «bot». Por ejemplo: TetrisBot o tetris_bot."
7. Nombra a tu bot con un nombre y luego añadele ´bot´ → debe terminar en <bot> sino BotFather te votara "Sorry, this username is invalid" (Anecdota: he puesto AutomatizacionReelsBot y me boto error, puse lo mismo insistiendole y me boto error nuevamente, probe con "MiNombre"ReelMonitor_bot y me acepto y respondio)
8. Te enviara un mensaje que se vera asi " Done! Congratulations on your new bot. You will find it at t.me/"MiNombre"ReelMonitor_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
Use this token to access the HTTP API:
  **547856584:BBCzaFttr985rf5LlHP7qJ02T37SoruYEOVS**  
Keep your token secure and store it safely, it can be used by anyone to control your bot.
For a description of the Bot API, see this page: https://core.telegram.org/bots/api "
9. COPIA lo que este OCUPANDO el "**547856584:BBCzaFttr985rf5LlHP7qJ02T37SoruYEOVS**" ese es tu TELEGRAM_BOT_TOKEN que necesitamos
10. Pega el TELEGRAM_BOT_TOKEN en un bloc de notas para guardarlo
Listo, ahora ya tienes creado el Bot de telegram, y tambien el TELEGRAM_BOT_TOKEN, que es la 4ta variable de las 5 variables que necesita el sistema para funcionar

**12. Genera el TELEGRAM_CHAT_ID**
1. Ve a Google
2. Remplaza en este link "https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates" remplazando el "{TELEGRAM_BOT_TOKEN}" por tu TELEGRAM_BOT_TOKEN que generamos en el paso 11 y pon el nuevo link en el navegador
3. Dale Enter (Si te bota:<br>
                          {<br>
                           "ok": false,<br>
                           "error_code": 401,<br>
                          "description": "Unauthorized"<br>
                          }<br>
                          Revisa el https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates que te dije que modificaras, probablemente este mal)

5. Te deberia salir: {<br>
                       "ok": true,<br>
                       "result": [ <br>
                         { <br>
                           "update_id": ..., <br>
                           "message": { <br>
                             "message_id": ..., <br>
                             "from": {...}, <br>
                             "chat": { <br>
                               "id": 123456789, <br>
                               "first_name": "Rendal", <br>
                               ... <br>
                             }, <br>
                             ... <br>

6. El número dentro de **"chat": {"id": ...}** es tu TELEGRAM_CHAT_ID → cópialo y abre un bloc de notas y pegalo
Listo ya tenemos el TELEGRAM_CHAT_ID, que es la 5ta variable de las 5 variables que necesita el sistema para funcionar

Listo con esto ya tenemos las 5 variables ahora es momento de dejar de buscar y empezar a construir

**13. Configura los 5 Secrets en GitHub**
1. Entra a https://github.com/
2. Donde dice "Top repositories" → dale click al Repositorio que se encuentra abajo de "Top repositories"
3. Dale click donde diga "Settings"
4. Dale clcik a "Secrets and variables"
5. Dale clcik a "Actions"
6. Dale clcik a "New repository secret"
Ahora ten cuidado haciendo exactamente lo que te digo...
En "Name" se pone el nombre que desees al secreto y en "Secret" se pone el valor que debemos ponerle al secreto
Ahora
7. En Name pon IG_ACCESS_TOKEN y en Secret pones el token del paso 8 y darle a "Add secret"
8. En Name pones IG_ACCESS_TOKEN y en Secret pones el token del paso 8
9. En Name pones IG_ACCESS_TOKEN y en Secret pones el token del paso 8
10. En Name pones IG_ACCESS_TOKEN y en Secret pones el token del paso 8
11. En Name pones IG_ACCESS_TOKEN y en Secret pones el token del paso 8
Listo, lo que acabamos de hacer es integrar las 5 variables en el sistema. Ahora solo falta hacer que el sistema guarde su propio progreso, permitir que el sistema pueda subir videos y caption y disparar automáticamente el sistema para que no tengas que hacerlo manualmente

**14. Haz que el sistema guarde su propio progreso. Activa permisos de escritura para Actions**
1. Entra a https://github.com/
2. Donde dice "Top repositories" → dale click al Repositorio que se encuentra abajo de "Top repositories"
3. Dale click donde diga "Settings" → "Actions" → "General" → "Workflow permissions" → selecciona "Read and write permissions" → y luego le das al boton "Save"
Con esto le dotas al sistema de guardar su propio progreso

**15. Permitire que el sistema pueda subir videos y captions. Crea una cuenta en Cloudinary**
1. Entra al link [cloudinary.com](https://cloudinary.com)
2. Create una cuenta en cloudinary
Listo, esto te permitirá subir tus videos al sistema en forma de URLs, que es mucho mas barato y practico

**16. Crea un disparador automático para el sistema. Create una cuenta y configura en cron-jub.org**
1. Entra al link [github.com/settings/tokens?type=beta](https://github.com/settings/tokens?type=beta)
2. Dale clic a "Generate new token".
3. En "Confirm access", confirma tu acceso (con tu contraseña o 2FA).
4. En "Token name", escribe algo como "trigger-publishme"
5. En "Expiration" → selecciona "No expiration"
6. En "Repository access", marca "Only select repositories" → y en el desplegable, dale click a tu repositorio
7. Baja hasta "Permissions" → dale clic a la pestaña "Repositories" (aparece junto a "Account") → dale clic a "Add permissions"
8. Busca "Actions" en la lista → y cámbialo de "Read-only" a "Read and write"
9. Baja y dale clic a "Generate token"
10. Y luego dale nuevamente "Generate token"
11. Copia el token que te muestra (empieza con "github_pat_...") y guárdalo en un lugar seguro — no lo vas a volver a ver después de esto, por eso cópialo y pégalo en algún lado
12. Dale click al link [cron-job.org](https://cron-job.org). y créate una cuenta
13. En el Panel, dale clic a "CREAR CRONJOB"
14. En "Título", escribe algo como "Disparar PublishMe"
15. En "Horario de ejecución", marca la opción "Cada" → cambia el número a 15 minutos.
16. Dale clic a la pestaña "AVANZADO" (arriba, junto a "COMÚN").
17. Baja hasta "Encabezados" → dale clic a "AÑADIR" dos veces, para crear estos dos encabezados:
<br>
 Clave : Authorization - Valor : Bearer {TU_TOKEN} (escribe "Bearer"y seguido tu token "github_pat_..." )<br>
 Clave : Accept - Valor : application/vnd.github+json<br>
18. En "Cuerpo de la solicitud", pega exactamente esto: "{"ref":"main"}"
19. Baja hasta el final → y dale a "EJECUCIÓN DE PRUEBA" (si te sale "204 No Content", significa que lo hiciste muy bien ;) ).
20. Luego cierra la ventana → y dale al botón naranja "Crear"
Listo, acabamos de crear el disparador automático del sistema para que no estés activándolo todo el tiempo manualmente

Listo, el sistema ya esta construido y la hora de Publicar contenido en Funcion al Rendimiento de tus reels (y ya no en funcion a las fechas) acaba de comenzar...

**Agrega tu primer reel a la cola de espera**
1. Entra a https://github.com/
2. Donde dice "Top repositories" → dale click al Repositorio que se encuentra abajo de "Top repositories"
3. Busca un archivo que dice "Formato para publicar reels en PublishMe"
4. Copia tu cantidad de formatos-reels que quieres usar o crear uno como lo dice el archivo
7. Busca un archivo llamado "reel_queue.json" → y dale click
8. Busca un lapiz en la parte derecha (cuando le pones el cursor encima aparece un texto que dice "edit this file") → y dale click
9. Pega lo que copiaste o creaste en "Formato para publicar reels en PublishMe"
10. Donde dice URL_DEL_VIDEO_DEL_REEL hay va la Url de tu video que quieres subir (entra a cludiinary → selecciona el bton subir en la parte derecha superior → sube tu video → aparecera tu video en la pantalla luego seleccionalo dandole dobe click → luego dale a "Compartir" o "Share" → luego dale a "Empotrar" → luego dale a "Configuracion del video" y luego a "Enlace" y luego copia ese link que te aparece abajo → ese es tu URL_DEL_VIDEO_DEL_REEL) y remplaza ese texto "URL_DEL_VIDEO_DEL_REEL" por el url que conseguimos
11. Donde dice TEXTO_QUE_APARECERA_EN_LA_DESCRIPCION pones lo que vas a poner en la descripción de tu video, remplaza ese TEXTO_QUE_APARECERA_EN_LA_DESCRIPCION por la descripción de tu video
12. Luego le das a "Commit changes o Confirmar los cambios"
Listo, haz esto con cada video y ya estarás subiendo tus videos al sistema y se irán publicando en funcion al rendimineto<br>

Ahora es hora de configurar el sistema para que decida en función a tus criterios<br>

**Ajusta PublishMe a tu estilo de creador**
1. Busca el archivo que dice "reel_death_trigger.py"
2. Entre todo el codigo busca lineas que digan:<br>
   **SLOPE_THRESHOLD** = 2.0<br>
   **CONSECUTIVE_READINGS_REQUIRED** = 3<br>
   **GRACE_PERIOD_HOURS** = 3<br>
   **MERIT_GRACE_TRIGGER_SLOPE** = 5.0<br>
   **MERIT_GRACE_HOURS** = 24<br>
   <br>
   Estos valores viven dentro de reel_death_trigger.py.<br>
   Estos valores (el 2.0,3,3,5.0,24) son valores míos<br>
   que mas que valores son patrones, patrones<br>
   en mis contenidos como creador de contenido.<br>
   No hay valores "correctos" universales —<br>
   Experimenta con los tuyos.<br>

   **SLOPE_THRESHOLD**<br>

   El número de vistas/minuto mínimo que le<br>
   indica al sistema que un reel está<br>
   empezando a morir.<br>

   Sin esto: el sistema no distingue un<br>
   reel que sigue creciendo de uno que ya<br>
   se apagó. Publica al azar, o no publica<br>
   nunca.<br>
   Con esto: el sistema sabe exactamente<br>
   qué tan vivo tiene que seguir un reel<br>
   para seguir esperando.<br>

   **CONSECUTIVE_READINGS_REQUIRED**<br>

   El número de rachas malas seguidas que<br>
   tolera el sistema antes de dar por muerto a<br>
   un reel.<br>

   Sin esto: una sola lectura baja mata el<br>
   reel de inmediato. El ruido normal se<br>
   confunde con muerte real, y el<br>
   contenido se reemplaza antes de<br>
   tiempo.<br>
   Con esto: el reel tiene rachas<br>
   garantizadas para demostrar que se<br>
   estaba recuperando, antes de ser<br>
   reemplazado.<br>

   **GRACE_PERIOD_HOURS**<br>

   El número de horas, desde el momento de<br>
   publicación, que se le dan a todos tus reels<br>
   para respirar antes de evaluar si rinden o no.<br>

   Sin esto: el sistema mata reels recién<br>
   nacidos mientras Instagram todavía<br>
   los está probando con una audiencia<br>
   pequeña. Su rendimiento real nunca<br>
   llega a revelarse.<br>
   Con esto: cada reel tiene el tiempo<br>
   garantizado para mostrar su verdadero<br>
   potencial antes de ser juzgado.<br>

   **MERIT_GRACE_TRIGGER_SLOPE**<br>

   El número de vistas/minuto que tú, como<br>
   creador, defines como la señal de que un<br>
   reel está a punto de dispararse.<br>

   Sin esto: el sistema trata a un reel viral<br>
   exactamente igual que a uno<br>
   mediocre. No existe ninguna<br>
   diferencia entre los dos.<br>
   Con esto: el sistema reconoce el<br>
   momento exacto en que un reel<br>
   demuestra éxito excepcional.<br>

   **MERIT_GRACE_HOURS**<br>

   El número de horas de tolerancia que se<br>
   gana un reel apenas toca esa señal de éxito.<br>
   Sus rachas malas dejan de contar en su<br>
   contra durante ese tiempo.<br>

   Sin esto: un reel viral muere por una<br>
   caída puntual, en el momento exacto<br>
   en que más falta le hace seguir vivo<br>
   para capitalizar su alcance.<br>
   Con esto: un reel excepcional se gana<br>
   el beneficio de la duda, y sigue vivo<br>
   horas — o días, si repite la hazaña —<br>
   más que un reel normal.<br>









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
