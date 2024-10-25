from aiogram.enums import ParseMode

from functions.text_reader import TextReader
from keyboard.userkeyboard import get_user_keyboard, get_back_keyboard, get_start_keyboard



import asyncio

from aiogram import Router, F, html
from aiogram.filters import Command, callback_data
from aiogram.types import Message, CallbackQuery

import emoji

router = Router()



@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        emoji.emojize(
            f':waving_hand: Привет, {message.from_user.first_name} и добро пожаловать в TextSearcher, твой личный помощник по поиску информации в тексте!\n'
            f'\n:rocket: Представь: у тебя есть огромный текст, например, презентация, статья или книга. Нужно найти все предложения, где встречается конкретное слово, но вручную просматривать все слишком долго и утомительно?\n'
            f'\n:thought_balloon: Я могу сделать это за тебя! Просто введи слово, которое ты хочешь найти, и я быстро покажу тебе все предложения, где оно встречается.\n'
            f'\n:dizzy: Экономия времени, удобство и точность поиска - это то, что я предлагаю. Пробуй!'
        ),
        reply_markup=get_start_keyboard()
    )
    await message.delete()




@router.callback_query(F.data == "start_message")
async def main_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        emoji.emojize(
            f'{callback.from_user.first_name}, ваша статистика:notebook_with_decorative_cover::\n'
            f'    -Количество поисков : \n'
            f'    -Количество найденных предложений в сообщениях: \n'
            f'    -Количество найденных предложений в файлах: ', ),
        reply_markup= get_user_keyboard()

    )


@router.callback_query(F.data == "search_few_files")
async def message_reader(callback: CallbackQuery):
    await callback.message.edit_text("Отправь мне несколько файлов")
    await callback.message.edit_reply_markup(reply_markup=get_back_keyboard())
    await callback.answer()


@router.callback_query(F.data == "get_back")
async def message_back(callback: CallbackQuery):
    await callback.message.edit_text(
        emoji.emojize(
            f'{callback.from_user.first_name}, ваша статистика:notebook_with_decorative_cover::\n'
            f'    -Количество поисков : \n'
            f'    -Количество найденных предложений в сообщениях: \n'
            f'    -Количество найденных предложений в файлах: ',     ),
        reply_markup=get_user_keyboard()
    )
    await callback.message.edit_reply_markup(reply_markup=get_user_keyboard())


