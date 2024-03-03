import os
from aiohttp import web
from aiogram.types import Update
from loader import bot, dp
from handlers.commands import router
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

WEBAPP_HOST = os.getenv('BOT_WEBAPP_HOST')
WEBAPP_PORT = int(os.getenv('BOT_WEBAPP_PORT'))
WEBHOOK_URL = os.getenv('BOT_WEBHOOK_URL')


async def handle_webhook(request):
    data = await request.json()
    update = Update(**data)
    await dp.feed_update(bot=bot, update=update)
    return web.Response(text="OK")

async def on_startup(app: web.Application):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app: web.Application):
    await bot.delete_webhook()
    await bot.session.close()

def main():
    dp.include_router(router)
    app = web.Application()
    app.router.add_post('/webhook/path', handle_webhook)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)

if __name__ == '__main__':
    main()
