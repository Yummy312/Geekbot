from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from random import choice
import os
TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
os.chdir('media')


@dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    div_button = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Next", callback_data='button_1')
    div_button.add(button_1)

    question = "Кортеж это какой тип данных?"
    answer = [
        'изменяемый',
        'неизменяемый' ,
        'двоичный',
        'волнообразный',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        type='quiz',
        correct_option_id=1,
        open_period=20,
        explanation='УПС',
        reply_markup=div_button,
        is_anonymous=False

    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Кто снимался в фильме Форсаж?"
    answer = [
        'Доминик Торрето',
        'Джеки Чан',
        'Пол Уокер',
        'Вин Дизель',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        open_period=17,
        correct_option_id=2 or 3,
        type='quiz',
        is_anonymous=False
    )


@dp.message_handler(commands=['mem'])
async def mem_send(message: types.Message):
    list_photos = os.listdir(f'{os.getcwd()}')
    photo = open(os.getcwd()+'\\'+choice(list_photos), 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler()
async def start_pooling(message: types.Message):
    if message.text.isdigit():
        num = int(message.text)
        res = num*num

        await bot.send_message(message.from_user.id, str(res))
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






