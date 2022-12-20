from aiogram.utils import executor
from config import dp
from handlers import register_callback_query_handlers, register_message_handlers, register_extra_handlers, register_fsm_handlers

register_message_handlers(dp)
register_fsm_handlers(dp)
register_callback_query_handlers(dp)
register_extra_handlers(dp)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






