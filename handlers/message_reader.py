from main import bot

from functions.text_reader import TextReader

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
router = Router()
storage = MemoryStorage()

@router.message(F.text)
async def message_read(message: Message):
    text_reader = TextReader(message.text, "Python")
    sentences = text_reader.send_matching_sentences()
    await message.answer(sentences)