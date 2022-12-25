from config import bot, dp
from aiogram import types, Dispatcher
from keyboard import clent_kb
from config import ADMIN
from random import choice


async def start_pooling(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id != ADMIN:
            await message.answer('Вы не админ и поэтому данная функция для вас недоступна')
        else:
            if message.text.startswith('game'.lower()):
                emoji_ls = ['⚽', '🏀', '🎲', '🎯', '🎳', '🎰']
                await bot.send_dice(message.chat.id, emoji=choice(emoji_ls))

            if not message.reply_to_message and message.text == '!pin':
                await message.answer('Команда должна быть ответом на сообщение')
            else:
                if message.text == '!pin':
                    await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

    elif message.chat.type == 'private':
        if message.text.isdigit():
            num = int(message.text)
            res = num * num
            await bot.send_message(message.from_user.id, str(res))

        elif message.text == 'start':
            await bot.send_message(message.from_user.id, text="it's ready!", reply_markup=clent_kb.keyboard_window)


def register_extra_handlers(dp: Dispatcher):
    dp.register_message_handler(start_pooling)
