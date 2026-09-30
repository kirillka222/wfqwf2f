from telethon import TelegramClient, events
import random
import time
import string

api_id = ''
api_hash = ''

client = TelegramClient('jr3edqwdqwdqwgije', api_id, api_hash)
client.start()

@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Город' in event.raw_text:
        await event.respond('💌Сообщение')
    time.sleep(0)  # это задержка, можешь убрать (Поставить 0)(не рекомендую)

@client.on(events.NewMessage)
async def my_event_handler(event):
    if '✍️Введите текст/🎙Запишите голосовое' in event.raw_text:
        await event.respond('')
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Теперь поставьте оценку пользователю' in event.raw_text:
        await event.respond('10')  # тут оценку которая поставится
    time.sleep(0.5)  # это задержка, можешь убрать (Поставить 0)(не рекомендую)

@client.on(events.NewMessage)
async def handle_rate_button(event):
    if '😏 Хочешь анонимную оценку своей анкеты?' in event.raw_text:
        await event.respond('🚀Оценивать')

client.run_until_disconnected()
