from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from keyboard.settings_kb import set_settings_keyboard

router = Router()


@router.message(Command("settings"))
async def set_settings(message: Message):
    await message.answer("Поменяйте ваши настройки поиска:", reply_markup=set_settings_keyboard())