import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher


load_dotenv()

__TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = Bot(__TELEGRAM_TOKEN)
dp = Dispatcher()