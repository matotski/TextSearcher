import emoji
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def get_settings_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text=emoji.emojize("Настройки :hammer_and_wrench:"))
    return builder.as_markup(resize_keyboard = True)

def set_settings_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=emoji.emojize("Учет регистра :cross_mark:"),callback_data="is_register")
    builder.button(text=emoji.emojize("Точный поиск :check_mark:"), callback_data="is_exact")
    builder.button(text=emoji.emojize("Замена текста:cross_mark:"), callback_data="is_replacement")
    builder.adjust(1)
    return builder.as_markup()