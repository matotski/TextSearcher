import aiogram.types

from config import config


from handlers import menu_handler, set_settings, message_reader


import asyncio
import logging

from aiogram import Bot, Dispatcher



logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())
from database.engine import create_db
dp = Dispatcher()

async def on_startup(bot):
    await create_db()

async def main():

    dp.startup.register(on_startup)
    dp.include_routers(menu_handler.router,set_settings.router, message_reader.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())