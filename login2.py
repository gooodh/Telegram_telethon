import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError


from config import api_id, api_hash


async def custom_phone_input():
    """Функция custom_phone_input запрашивает у пользователя
    ввод номера телефона и возвращает его."""
    return await asyncio.get_event_loop().run_in_executor(
        None, input, "Введите ваш номер телефона: "
    )


async def custom_code_input():
    """Функция custom_code_input запрашивает у пользователя
    ввод кодa и возвращает его."""
    return await asyncio.get_event_loop().run_in_executor(
        None, input, "Введите код, который вы получили: "
    )


async def custom_password_input():
    """Функция custom_password_input запрашивает у пользователя
    ввод пароля и возвращает его."""
    return await asyncio.get_event_loop().run_in_executor(
        None, input, "Введите ваш пароль: "
    )


async def main():
    """Этот код содержит функцию main, которая используется для
    запуска клиента Telegram. Функция создает нового клиента TelegramClient
    с указанным API ID и API hash. Затем функция запускает клиент и передает
    функции custom_phone_input, custom_code_input и custom_password_input
    для ввода номера телефона, кода подтверждения и пароля соответственно.
    Если требуется код подтверждения или пароль, функция запрашивает их у
    пользователя. После этого функция отправляет сообщение в чат."""
    client = TelegramClient("anon", api_id, api_hash)

    # Запускаем клиент и передаем пользовательский ввод телефона
    await client.start(
        phone=custom_phone_input,
        code_callback=custom_code_input,
        password=custom_password_input,
    )

    # Если требуется код подтверждения
    try:
        await client.sign_in()
    except SessionPasswordNeededError:
        # Если требуется пароль, запрашиваем его
        password = await custom_password_input()
        await client.sign_in(password=password)

    # Запрашиваем код подтверждения, если это необходимо
    if not client.is_user_authorized():
        code = await custom_code_input()
        await client.sign_in(code=code)

    # Используем свою фразу для ввода сообщения
    user_input = await custom_input("Введите ваше сообщение: ")

    # Отправляем сообщение в чат (например, в личные сообщения самому себе)
    me = await client.get_me()  # Получаем информацию о себе
    await client.send_message(me, user_input)  # Отправляем сообщение

    print(f"Сообщение отправлено: {user_input}")


async def custom_input(prompt):
    print(prompt, end="", flush=True)
    return await asyncio.get_event_loop().run_in_executor(None, input)


# Запуск основного цикла
if __name__ == "__main__":
    asyncio.run(main())
