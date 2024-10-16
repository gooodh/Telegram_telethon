from telethon import TelegramClient

async def connect_and_send_message(api_id, api_hash, phone_number, session_name, message, chat_id):
    # Создаем клиент
    client = TelegramClient(session_name, api_id, api_hash)
    
    # Подключаемся к аккаунту
    await client.start(phone=phone_number)
    print(f"{session_name} подключен")

    # Отправляем сообщение
    await client.send_message(chat_id, message)
    print(f"Сообщение отправлено из {session_name}")

    # Закрываем клиент
    await client.disconnect()

async def main():
    # Данные для первого аккаунта
    api_id_1 = 'YOUR_API_ID_1'
    api_hash_1 = 'YOUR_API_HASH_1'
    phone_number_1 = 'YOUR_PHONE_NUMBER_1'
    session_name_1 = 'session1'
    message_1 = 'Привет от первого аккаунта!'
    chat_id_1 = 'username_or_chat_id_1'  # Замените на реальный ID или имя пользователя

    # Данные для второго аккаунта
    api_id_2 = 'YOUR_API_ID_2'
    api_hash_2 = 'YOUR_API_HASH_2'
    phone_number_2 = 'YOUR_PHONE_NUMBER_2'
    session_name_2 = 'session2'
    message_2 = 'Привет от второго аккаунта!'
    chat_id_2 = 'username_or_chat_id_2'  # Замените на реальный ID или имя пользователя

    # Запускаем функции для каждого аккаунта
    await connect_and_send_message(api_id_1, api_hash_1, phone_number_1, session_name_1, message_1, chat_id_1)
    await connect_and_send_message(api_id_2, api_hash_2, phone_number_2, session_name_2, message_2, chat_id_2)

# Запускаем основной цикл
import asyncio
asyncio.run(main())
