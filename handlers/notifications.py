import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot, ADMIN, PATH


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = ADMIN
    await message.answer('I have got id')


async def send_new_words():
    with open(f"{PATH}/eng_words.txt", 'r') as file:
        content = file.readlines()
        word_count = 0
        for word in content:
            await bot.send_message(chat_id=chat_id, text=f"{word}")
            word_count += 1
            if word_count == 10:
                break


async def start_notifications():
    aioschedule.every().friday.at('14:00').do(send_new_words)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_notification_handlers(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: "напомни".lower() in word.text)
