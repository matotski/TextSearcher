import aiogram.types

from config import config

from handlers import message_reader, set_settings

import asyncio
import logging

from aiogram import Bot, Dispatcher



logging.basicConfig(level=logging.INFO)



async def main():
    dp = Dispatcher()
    bot = Bot(token=config.bot_token.get_secret_value())
    dp.include_routers(message_reader.router,set_settings.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())