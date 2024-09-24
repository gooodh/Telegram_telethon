from telethon import TelegramClient, events

from config import api_id, api_hash


client = TelegramClient('anon', api_id, api_hash)
await client.connect()
await client.loi
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')


@client.on(events.NewMessage(pattern=r'(?i).*heck'))
async def handler(event):
    await event.delete()


client.start()
client.run_until_disconnected()
