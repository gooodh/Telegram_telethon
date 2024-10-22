import asyncio

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, FloodWaitError

from telethon.tl.types import PeerChannel, ChannelParticipantsSearch

from config import api_id, api_hash, phone



api_hash = str(api_hash)

client = TelegramClient("anon", api_id, api_hash)

async def fetch_participants(channel):
    '''getting all users of the group by the limit, written by gpt'''
    participants = await client(GetParticipantsRequest(
        channel,
        offset=0,
        limit=500,  # Настройте по мере необходимости
        filter=ChannelParticipantsSearch(''),  # Вы можете фильтровать, если нужно
        hash=0
    ))
    return participants.users

async def main(phone):
    await client.start()
    print("Client Created")
    
    # Проверка авторизации
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Введите код: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Пароль: '))

    me = await client.get_me()
    user_input_channel = input('Введите идентификатор канала (URL или ID): ')

    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel

    my_channel = await client.get_entity(entity)

    # Получение участников канала
    try:
        participants = await fetch_participants(my_channel)
        all_users = [user.id for user in participants]
        print(f'Все пользователи: {len(all_users)}')
    except FloodWaitError as e:
        print(f"Ошибка Flood wait: {e}")
        await asyncio.sleep(e.seconds)  # Ждем указанное количество секунд

with client:
    client.loop.run_until_complete(main(phone))
