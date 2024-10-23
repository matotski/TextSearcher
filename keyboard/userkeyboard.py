from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

import emoji

def get_start_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=emoji.emojize("Начать :rocket:"), callback_data="start_message")
    return builder.as_markup()

def get_user_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=emoji.emojize("Поиск по тексту :orange_book:"),callback_data="search_message")
    builder.button(text=emoji.emojize("Поиск по файлу :green_book:"),callback_data="search_file")
    builder.button(text=emoji.emojize("Поиск по нескольким файлам:books:",),callback_data="search_few_files")
    builder.adjust(2)
    return builder.as_markup()

def get_back_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=emoji.emojize("Назад :BACK_arrow:"), callback_data="get_back")
    return builder.as_markup()

