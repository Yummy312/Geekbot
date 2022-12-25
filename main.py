from aiogram.utils import executor
from config import dp
from handlers import register_callback_query_handlers, register_message_handlers, register_extra_handlers,\
    register_fsm_handlers, register_admin_handlers
from database import create_bot_db

register_message_handlers(dp)
register_callback_query_handlers(dp)
register_admin_handlers(dp)
register_fsm_handlers(dp)
register_extra_handlers(dp)


async def on_startup(_):
    create_bot_db()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)






