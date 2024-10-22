import json
import asyncio
from datetime import date, datetime
import time

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError

from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
from config import api_id, api_hash, phone


# some functions to parse json date
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return list(o)

        return json.JSONEncoder.default(self, o)


# Setting configuration values

api_hash = str(api_hash)

# Create the client and connect
client = TelegramClient("anon", api_id, api_hash)


async def main(phone):
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input("Enter the code: "))
        except SessionPasswordNeededError:
            await client.sign_in(password=input("Password: "))

    me = await client.get_me()

    user_input_channel = input("enter entity(telegram URL or entity id):")

    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel

    my_channel = await client.get_entity(entity)

    offset_id = 0
    limit = 100
    all_users = []
    total_user = 0
    total_count_limit = 99

    while True:
        try:
            history = await client(
                GetHistoryRequest(
                    peer=my_channel,
                    offset_id=offset_id,
                    offset_date=None,
                    add_offset=0,
                    limit=limit,
                    max_id=0,
                    min_id=0,
                    hash=0,
                )
            )
            if not history.messages:
                break
            messages = history.messages
            for message in messages:
                sender_id = message.sender_id
                if sender_id:
                    sender = await client.get_entity(sender_id)
                    all_users.append(sender.id)
                else:
                    print("Sender is None (likely a channel message)")
            offset_id = messages[len(messages) - 1].id

            total_user = len(set(all_users))
            if total_count_limit != 0 and total_user >= total_count_limit:
                print(f"Set all_users: {set(all_users)}")

                break
        except FloodWaitError as e:
            print(f"Ошибка Flood wait: {e}")
            time.sleep(e.seconds)


with client:
    client.loop.run_until_complete(main(phone))
