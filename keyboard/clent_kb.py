from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_window = ReplyKeyboardMarkup(
    resize_keyboard=True
)

quiz_button = KeyboardButton('/quiz')
mem_button = KeyboardButton('/mem')
keyboard_window.add(quiz_button, mem_button)

'''Кнопки для fsm'''
cancel_button = KeyboardButton('CANCEL')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(cancel_button)

backend = KeyboardButton('backend')
frontend = KeyboardButton('frontend')
fullstack = KeyboardButton('fullstack')
direct_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2,
).add(backend, frontend, fullstack, cancel_button)

submit_yes = KeyboardButton('да')
submit_no = KeyboardButton('нет')
submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(submit_yes, submit_no)



