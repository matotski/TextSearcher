from config import config
from handlers import menu_handler, set_settings, message_reader, text_file_message_reader
import asyncio
import logging
from bot_cmd import commands
from aiogram.types import BotCommandScopeAllPrivateChats
from aiogram import Bot, Dispatcher


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

from database.engine import create_db


async def on_startup(bot):
    await create_db()


async def main():
    dp.startup.register(on_startup)
    await bot.set_my_commands(commands=commands,scope=BotCommandScopeAllPrivateChats())
    dp.include_routers(
        menu_handler.router,
        set_settings.router,
        message_reader.router,
        text_file_message_reader.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())