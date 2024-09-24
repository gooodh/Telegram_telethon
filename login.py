import asyncio
from telethon import TelegramClient
from telethon.types import User

from config import api_id, api_hash

# Задай свои переменные SESSION, API_ID, API_HASH
async def main():
    client = TelegramClient('SESSION', api_id, api_hash)
    await client.start()
# async def main():
#     async with TelegramClient('SESSION', api_id, api_hash) as client:
#         if not await client.is_authorized():
#             phone = input('Введите номер телефона: ')
#             await client.send_code_request(phone)
#             code = input('Введите код: ')

        #     try:
        #         user = await client.sign_in(phone, code)
        #     except Exception as e:
        #         print(f'Ошибка при входе: {e}')
        #         return

        #     if isinstance(user, User):
        #         print(f'Добро пожаловать, {user.first_name}! 😊')
        #     else:
        #         # Возможно, это PasswordToken
        #         password_token = user
        #         import getpass
        #         password = getpass.getpass("Введите пароль: ")
        #         try:
        #             user = await client.check_password(password_token, password)
        #             print(f'Добро пожаловать снова, {user.first_name}! 😊')
        #         except Exception as e:
        #             print(f'Ошибка при проверке пароля: {e}')


asyncio.run(main())
