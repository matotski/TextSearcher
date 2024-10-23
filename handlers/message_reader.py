from functions.text_reader import find_sentences_in_message
import asyncio
from aiogram import Router, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

@router.message(F.text)
async def message_read(message: Message):
    sentences = find_sentences_in_message(message.text, "город")
    answer = f'Слово было найдено {len(sentences)} раз\n'
    for i in range(len(sentences)):
        answer += f'Предложение {i}: {sentences[i]}\n'
    await message.answer(answer)
