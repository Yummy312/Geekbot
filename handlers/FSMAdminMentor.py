import re
import string
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from config import ADMIN
from keyboard.clent_kb import direct_markup, submit_markup, cancel_markup


class FSMAdmin(StatesGroup):
    id_mentor = State()
    name_mentor = State()
    direct_mentor = State()
    age_mentor = State()
    group_mentor = State()
    submit = State()


async def start_fsm(message: types.Message):
    if message.from_user.id != ADMIN:
        await message.answer('Функция доступна только для админа!')
    else:
        await FSMAdmin.id_mentor.set()
        await message.answer('id ментора?', reply_markup=cancel_markup)


async def load_id_mentor(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('id должен состоять только из цифр')
    elif message.text.isdigit():
        if len(message.text) != 10:
            await message.answer('id должен содержать не менее 10 цифр')
        else:
            async with state.proxy() as data:
                data['id_mentor'] = message.text
            await FSMAdmin.next()
            await message.answer('Имя ментора?', reply_markup=cancel_markup)


async def load_name_mentor(message: types.Message, state: FSMContext):
    if not message.text.isalpha():
        if [i for i in message.text if i in string.digits]:
            await message.answer('Имя не должно содержать цифр')
        else:
            await message.answer('В имени присутствуют недопустимые символы.')
    else:
        async with state.proxy() as data:
            data['name_mentor'] = message.text
        await FSMAdmin.next()
        await message.answer('Направление ментора', reply_markup=direct_markup)


async def load_direct_mentor(message: types.Message, state: FSMContext):
    direct = ['backend', 'frontend', 'fullstack']
    if message.text not in direct:
        await message.answer('Такого направления нет')
    else:
        async with state.proxy() as data:
            data['direct_mentor'] = message.text
        await FSMAdmin.next()
        await message.answer('Какой возраст?', reply_markup=cancel_markup)


async def load_age_mentor(message: types.Message, state: FSMContext):
    normal_age = [str(i) for i in range(17, 60)]

    if not message.text.isdigit():
        await message.answer('Пиши только число')

    elif message.text.isdigit() and message.text not in normal_age:
        await message.answer('Возрастное ограничение')
    else:
        async with state.proxy() as data:
            data['age_mentor'] = message.text
        await FSMAdmin.next()
        await message.answer('какая группа?', reply_markup=cancel_markup)


async def load_group_mentor(message: types.Message, state: FSMContext):
    example = re.findall(r'[a-zA-Z-]+[1-9]+', message.text)
    print(len(example))
    if len(example) <= 0:
        await message.answer(f'Неправильное название группы. Нужно писать так, например\nPy-21 или UX-UI-12')
    else:
        async with state.proxy() as data:
            data['group_mentor'] = message.text
        await FSMAdmin.next()
        await message.answer(f"id_ментора: {data['id_mentor']}\nИмя ментора: {data['name_mentor']}"
                                          f"\nНаправление: {data['direct_mentor']}"
                                          f"\nВозраст: {data['age_mentor'] }\nГруппа: {data['group_mentor']}",)

        await message.answer('Все верно?', reply_markup=submit_markup)


async def submit_fsm(message: types.Message, state: FSMContext):
    if message.text not in ['да', 'нет']:
        await message.answer('Выбери ответ из списка!')
    else:
        if message.text.lower() == 'да':
            await state.finish()
            await message.answer('Ты зареган')
        elif message.text.lower() == 'нет':
            await state.finish()
            await message.answer('Не хочешь, не надо!')


async def cancel_fsm(message:types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Регистрация отменена')


def register_fsm_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm,  state='*', commands=['cancel'])
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state='*',)
    dp.register_message_handler(start_fsm, commands=['reg'])
    dp.register_message_handler(load_id_mentor, state=FSMAdmin.id_mentor)
    dp.register_message_handler(load_name_mentor, state=FSMAdmin.name_mentor)
    dp.register_message_handler(load_direct_mentor, state=FSMAdmin.direct_mentor)
    dp.register_message_handler(load_age_mentor, state=FSMAdmin.age_mentor)
    dp.register_message_handler(load_group_mentor, state=FSMAdmin.group_mentor)
    dp.register_message_handler(submit_fsm, state=FSMAdmin.submit)
