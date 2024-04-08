import asyncio
import time
import pandas as pd
import datetime
import configparser
from telethon.sync import TelegramClient
import telegram
import os

# Configuración del bot de Telegram
config = configparser.ConfigParser()
config.read("telethon.config")

id_group = '-4197939437'
token_bot = '7155994571:AAGRGwXXoSfp3b1TOF2Axnnuwl82fUSklmY'
msg_info = telegram.Bot(token=token_bot)

# Carpeta para guardar las fotos
photo_folder = "fotos"

# Función para enviar mensajes al grupo de Telegram
async def send_msg_bot(msg):
    await msg_info.send_message(chat_id=id_group, text=msg)

# Datos de mi telegram
api_id = 26106430
api_hash = "d5bfd7d2b8567b459f253e91597141e0"
chats = ['criptonorberok']
specific_users = [1619215840,1476022128,5902973409,996496469,1777725742]

# Función principal para manejar el bucle de mensajes
async def main():
    # Guarda el tiempo de inicio de la ejecución del código
    start_time = datetime.datetime.now()

    # Leer el último mensaje procesado
    try:
        with open("last_processed_message_id.txt", "r") as file:
            last_processed_message_id = int(file.read())
    except (FileNotFoundError, ValueError):
        last_processed_message_id = None

    # Mantener un conjunto de IDs de mensajes procesados
    processed_message_ids = set()

    # Obtiene la ruta absoluta al directorio actual
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Especifica la ruta relativa al archivo de sesión
    session_file = os.path.join(current_directory, "test.session")

    # Carpeta completa para guardar las fotos
    photo_folder_path = os.path.join(current_directory, photo_folder)

    # Crea la carpeta si no existe
    if not os.path.exists(photo_folder_path):
        os.makedirs(photo_folder_path)

    # Intentar varias veces con un breve retraso en caso de error
    for _ in range(3):
        try:
            async with TelegramClient(session_file, api_id, api_hash) as client:
                while True:
                    data_list = []
                    for chat in chats:
                        async for message in client.iter_messages(chat, offset_date=start_time, reverse=True):
                            if message.id in processed_message_ids:
                                continue  # Si el mensaje ya está procesado, lo omitimos
                            if message.sender_id in specific_users:
                                if message.sender_id == 1476022128:
                                    print(f"CriptoNorber: {message.text}")
                                    if message.photo:  # Verifica si el mensaje contiene una foto
                                        # Descarga la foto y guarda en la carpeta de fotos
                                        photo_path = await message.download_media(file=os.path.join(photo_folder_path, f"{message.id}.jpg"))
                                        # Envía la foto al grupo
                                        await msg_info.send_photo(chat_id=id_group, photo=photo_path, caption=message.text)
                                        # Después de enviar la foto, eliminarla del sistema de archivos
                                        os.remove(photo_path)
                                    else:
                                        msg = f'CriptNorber: {message.text}'
                                        await send_msg_bot(msg)
                                elif message.sender_id == 5902973409:
                                    print(f"Esteban: {message.text}")
                                    if message.photo:
                                        photo_path = await message.download_media(file=os.path.join(photo_folder_path, f"{message.id}.jpg"))
                                        await msg_info.send_photo(chat_id=id_group, photo=photo_path, caption=message.text)
                                        os.remove(photo_path)
                                    else:
                                        msg = f'Esteban: {message.text}'
                                        await send_msg_bot(msg)
                                elif message.sender_id == 1619215840:
                                    print(f"Oso: {message.text}")
                                    if message.photo:
                                        photo_path = await message.download_media(file=os.path.join(photo_folder_path, f"{message.id}.jpg"))
                                        await msg_info.send_photo(chat_id=id_group, photo=photo_path, caption=message.text)
                                        os.remove(photo_path)
                                    else:
                                        msg = f'Oso: {message.text}'
                                        await send_msg_bot(msg)
                                
                                elif message.sender_id == 996496469:
                                    print(f"Cripto Aprendices: {message.text}")
                                    if message.photo:
                                        photo_path = await message.download_media(file=os.path.join(photo_folder_path, f"{message.id}.jpg"))
                                        await msg_info.send_photo(chat_id=id_group, photo=photo_path, caption=message.text)
                                        os.remove(photo_path)
                                    else:
                                        msg = f'Cripto Aprendices: {message.text}'
                                        await send_msg_bot(msg)
                                elif message.sender_id == 1777725742:
                                    print(f"Esteban: {message.text}")
                                    if message.photo:
                                        photo_path = await message.download_media(file=os.path.join(photo_folder_path, f"{message.id}.jpg"))
                                        await msg_info.send_photo(chat_id=id_group, photo=photo_path, caption=message.text)
                                        os.remove(photo_path)
                                    else:
                                        msg = f'Esteban: {message.text}'
                                        await send_msg_bot(msg)
                                    
                                else:
                                    print(f"{message.sender_id}: {message.text}")
                                    if message.photo:
                                        photo_path = await message.download_media(file=os.path.join(photo_folder_path, f"{message.id}.jpg"))
                                        await msg_info.send_photo(chat_id=id_group, photo=photo_path, caption=message.text)
                                        os.remove(photo_path)
                                    else:
                                        msg = f"{message.sender_id}: {message.text}"
                                        await send_msg_bot(msg)
                                    
                                processed_message_ids.add(message.id)
                                if message.date is not None:
                                    data = {"group": chat, "sender": message.sender_id, "text": message.text, "date": message.date}
                                    data_list.append(data)

                    if data_list:
                        df = pd.DataFrame(data_list)
                        df['date'] = pd.to_datetime(df['date']).dt.tz_localize(None)

                    time.sleep(1)  # Espera 1 segundo antes de volver a intentar

        except Exception as e:
            print("Error:", e)
            print("Reconnecting...")
            continue  # Reinicia el bucle en caso de error

    # Guardar el ID del último mensaje procesado para la próxima ejecución
    if last_processed_message_id:
        with open("last_processed_message_id.txt", "w") as file:
            file.write(str(last_processed_message_id))

# Ejecuta la función principal utilizando asyncio.run()
asyncio.run(main())
