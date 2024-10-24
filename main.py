import aiogram.types

from config import config

from handlers import menu_handler, set_settings

import asyncio
import logging

from aiogram import Bot, Dispatcher



logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())

async def main():
    dp = Dispatcher()

    dp.include_routers(menu_handler.router,set_settings.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())