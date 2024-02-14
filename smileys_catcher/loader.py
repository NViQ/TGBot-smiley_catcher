import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TOKEN = os.getenv('BOT_TOKEN')
WEBAPP_HOST = os.getenv('BOT_WEBAPP_HOST')
WEBAPP_PORT = os.getenv('BOR_WEBAPP_PORT')

bot = Bot(TOKEN, session=AiohttpSession(), parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
