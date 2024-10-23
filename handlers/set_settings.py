from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup

from keyboard.settings_kb import set_settings_keyboard

router = Router()

@router.message(F.text == "Настройки")
async def set_settings(message: Message):
    await message.answer("Поменяйте ваши настройки поиска:", reply_markup=set_settings_keyboard())