# library installation - https://docs.telethon.dev/en/stable/basic/installation.html
from telethon import TelegramClient, events

# Get the API id and hash from my.telegram.org
# ref: https://telegra.ph/How-to-get-Telegram-APP-ID--API-HASH-05-27
api_id = 12345
api_hash = '423908424390204032942904jsenweure'
client = TelegramClient('visa', api_id, api_hash)

# we can use regular expression
# more examples https://docs.telethon.dev/en/stable/basic/updates.html
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'avail' in event.raw_text:
        # send the message to other user or a personal channel
        await client.send_message(entity='dp_chennai_avail_channel', message='Check slots channel')

client.start()
client.run_until_disconnected()
