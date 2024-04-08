## Scrapper Telegram Bot

Este proyecto consiste en un bot de Telegram desarrollado en Python que proporciona funciones para la gestión y automatización de tareas en grupos de Telegram.

### Pasos para utilizar el bot:

1. **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/tu_usuario/Scrapper-Telegram-Bot.git
    ```

2. **Instalar Dependencias:**
    Asegúrate de tener Python instalado en tu sistema. Luego, instala las dependencias necesarias ejecutando:
    ```bash
    pip install -r requirements.txt
    ```

3. **Crear un Grupo en Telegram y Obtener su ID:**
    - Crea un grupo en Telegram.
    - Agrega tu bot recién creado al grupo.
    - Busca al bot `@userinfobot` en el grupo y mencionarlo con el comando `/id`.
    - El bot responderá con el ID del grupo. Guárdalo para configurar el bot.

4. **Obtener las Claves de Acceso:**
    - Para utilizar el bot, necesitarás obtener las claves de acceso necesarias:
        - `api_id` y `api_hash` para acceder a la API de Telegram.
        - `token_bot` para autenticar tu bot en Telegram.
    
    - Puedes obtener estas claves registrándote en el [Panel de Desarrolladores de Telegram](https://my.telegram.org/auth) y creando una nueva aplicación.

5. **Crear un Bot en Telegram:**
    - Abre Telegram y busca al bot `@BotFather`.
    - Sigue las instrucciones para crear un nuevo bot y obtener su token.

6. **Configurar el Bot:**
    - En el archivo `config.ini`, ingresa las claves de acceso obtenidas en los pasos anteriores:
        ```ini
        [Telegram]
        api_id = TU_API_ID
        api_hash = TU_API_HASH
        token_bot = TU_TOKEN_BOT
        ```
    - Además, puedes configurar otras opciones según tus necesidades.

7. **Ejecutar el Bot:**
    - Una vez configurado, puedes ejecutar el bot utilizando el siguiente comando:
        ```bash
        python main.py
        ```

8. **Interactuar con el Bot:**
    - Comienza a interactuar con tu bot en el grupo de Telegram según las funciones que hayas configurado.

### Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas de mejora, funcionalidades adicionales o correcciones de errores, no dudes en enviar un pull request.

### Licencia
Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT).
