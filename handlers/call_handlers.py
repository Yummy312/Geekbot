from config import bot, dp
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz_2(call: types.CallbackQuery):
    box_call = InlineKeyboardMarkup()
    call_button_1 = InlineKeyboardButton('Next', callback_data='call_button_1')
    box_call.add(call_button_1)
    question = "Кто снимался в фильме Форсаж?"
    answer = [
        'Доминик Торрето',
        'Джеки Чан',
        'Пол Уокер',
        'Брайан',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        open_period=17,
        correct_option_id=2,
        type='quiz',
        is_anonymous=False,
        reply_markup=box_call
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Что такое exceptions, <try-except>?"
    answer = [
        'Просто слова',
        'Исключения',
        'Общее описание алгоритмов',
        'Тип данных',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        correct_option_id=1,
        type='quiz',
        is_anonymous=False,
        open_period=23
    )


def register_callback_query_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_1')
    dp.register_callback_query_handler(quiz_3, text='call_button_1')