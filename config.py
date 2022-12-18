from aiogram import Bot, Dispatcher
from decouple import config
TOKEN = config("TOKEN")
ADMIN = config('ADMIN', cast=int)
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

