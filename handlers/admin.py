from aiogram import types, Dispatcher
from config import bot, ADMIN
from database import command_all_mentors_sql, command_delete_sql
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def show_all_mentors(message: types.Message):
    if message.from_user.id != ADMIN:
        await message.answer('Функция достпуна только для админа')
    else:
        mentors = await command_all_mentors_sql()
        for mentor in mentors:
            await bot.send_message(message.from_user.id,
                                   text=f"id: {mentor[0]}\nname: {mentor[1]}\ndirect: {mentor[2]}\n"
                                        f"age: {mentor[3]}\ngroup: {mentor[4]}")

        if not mentors:
            await message.answer('Нету зарегистрированных менторов')


async def delete_mentor(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id != ADMIN:
            await message.answer('Функция доступна  только для администратора')
        else:
            mentors = await command_all_mentors_sql()
            for mentor in mentors:
                await bot.send_message(message.from_user.id,
                                       text=f"id: {mentor[0]}\nname: {mentor[1]}\ndirect: {mentor[2]}\n"
                                            f"age: {mentor[3]}\ngroup: {mentor[4]}",
                                       reply_markup=InlineKeyboardMarkup().add
                                       (InlineKeyboardButton('DELETE', callback_data=mentor[0])))


async def complete_delete(call: types.CallbackQuery):
    await command_delete_sql(call.data)
    await call.answer(text='Удалено', show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(show_all_mentors, commands=['all'])
    dp.register_message_handler(delete_mentor, commands=['del'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data)
