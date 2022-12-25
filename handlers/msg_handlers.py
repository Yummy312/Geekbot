from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database import  random_choice_mentor
from config import bot, dp
from random import choice
import os


async def quiz(message: types.Message):
    div_button = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Next", callback_data='button_1')
    div_button.add(button_1)

    question = "Кортеж это какой тип данных?"
    answer = [
        'изменяемый',
        'неизменяемый',
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


async def mem_send(message: types.Message):
    file_list = []
    for filename in os.listdir('media'):
        file_list.append(filename)
    result = choice(file_list)
    photo = open(f'media/{result}', 'rb')
    print(photo)
    await bot.send_photo(message.chat.id, photo=photo)


async def get_random_mentors(message: types.Message):
    await random_choice_mentor(message)


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_message_handler(mem_send, commands=['mem'])
    dp.register_message_handler(get_random_mentors, commands=['random'])
