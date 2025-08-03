import asyncio
import random
from telethon import TelegramClient, events
from telethon.tl.types import DocumentAttributeVideo

api_id = 0 # здесь api_id (взять в https://telegram.org/)
api_hash = "0" # здесь api_hash (взять в https://telegram.org/)
bot_username = "bibinto_bot"
second_bot = "anonimnyi_chatbot"  # юзернейм любого другого анонимного чат бота
alert_user_id = 0 # здесь user_id своего основного аккаунта для отправки уведомлений о блокировке в бибинто

client = TelegramClient("userbot_session", api_id, api_hash)

def is_photo_or_video(msg):
    if msg.photo or msg.video:
        return True
    if msg.document:
        if getattr(msg.document, "mime_type", "").startswith("video/"):
            return True
        for attr in msg.document.attributes:
            if isinstance(attr, DocumentAttributeVideo):
                return True
    return False

# бибинто
@client.on(events.NewMessage(chats=bot_username, incoming=True))
async def handler(event):
    text = event.raw_text or ""
    if "Вы были заблокированы" in text:
        try:
            await client.send_message(alert_user_id, f"Обнаружено сообщение: {text}")
        except Exception:
            pass
    elif "Коала накушалась твоих оценок" in text:
        try:
            await client.send_message(alert_user_id, f"Обнаружено сообщение: {text}")
            await client.send_message(event.chat_id, f"⭐️Кто меня оценил?")
        except Exception:
            pass


    if is_photo_or_video(event.message):
        if "☝️Фотография оценщика☝️" in text:
            await asyncio.sleep(5)
            await client.send_message(event.chat_id, f"⭐️Кто меня оценил?")
            return
        await asyncio.sleep(3)
        choice = random.choice(["9", "8", "9", "10"])
        try:
            await client.send_message(event.chat_id, choice)
        except Exception:
            await client.send_message(alert_user_id, f"Обнаружено сообщение: {text}")

# анонимный чат
@client.on(events.NewMessage(chats=second_bot, incoming=True))
async def second_bot_handler(event):
    text = event.raw_text or ""

    if "Собеседник найден!" in text:
        await asyncio.sleep(2)
        await client.send_message(second_bot, "я д 17, tg свойтг")
        await asyncio.sleep(1)
        await client.send_message(second_bot, "/next")

    elif "Сначала подключите собеседника." in text:
        await asyncio.sleep(3)
        await client.send_message(second_bot, "/next")
    elif "Ваш собеседник прервал диалог" in text:
        await asyncio.sleep(2)
        await client.send_message(second_bot, "/next")

async def auto_sender1(): # отправка каждые 5 секунд в самый популярный 18+ чат тг
    while True:
        try:
            await client.send_message(-1001807169139, "🔞 привет, мне N и у меня есть свой канал с интересным контентом\n\nвсе есть в моем профиле, жду тебя!!!")
        except Exception:
            pass
        await asyncio.sleep(5)

async def auto_sender2(): # отправка каждые 20 секунд во второй 18+ чат тг
    while True:
        try:
            await client.send_message(-1002766517600, "🔞 привет, мне N и у меня есть свой канал с интересным контентом\n\nвсе есть в моем профиле, жду тебя!!!")
        except Exception:
            pass
        await asyncio.sleep(20)

@client.on(events.NewMessage(outgoing=True, pattern=r'^gte1$')) # заходите в нужный чат, пишите простое сообщение gte1 и у вас в консоли появится id чата
async def get_chat_id_handler(event):
    print(f"[chat_id] {event.chat_id}")

if __name__ == "__main__":
    client.start()
    client.loop.create_task(auto_sender1())
    client.loop.create_task(auto_sender2())
    client.run_until_disconnected()
