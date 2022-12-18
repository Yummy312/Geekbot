from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_window = ReplyKeyboardMarkup(
    resize_keyboard=True
)

quiz_button = KeyboardButton('/quiz')
mem_button = KeyboardButton('/mem')
keyboard_window.add(quiz_button, mem_button)