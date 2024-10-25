from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from nltk.corpus import words

from config import Settings
from handlers.menu_handler import message_back
from keyboard.userkeyboard import get_back_keyboard
from main import bot

from functions.text_reader import TextReader

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery


router = Router()


class SearchByWord(StatesGroup):
    text = State()
    word = State()

@router.callback_query(StateFilter(None),F.data == "search_message")
async def message_reader(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Отлично, отправь мне текст", reply_markup=get_back_keyboard(), parse_mode=ParseMode.HTML)
    await callback.answer()
    await state.set_state(SearchByWord.text)


@router.message(SearchByWord.text,F.text)
async def get_word(message: Message, state: FSMContext):
    await state.update_data(text = message.text)
    await message.answer("Супер! Теперь отправь мне искомое слово", reply_markup=get_back_keyboard())
    await state.set_state(SearchByWord.word)


@router.message(SearchByWord.word,F.text)
async def send_sentences(message: Message, state: FSMContext):
    await state.update_data(word = message.text)
    text_data = await state.get_data()
    text_reader = TextReader(text_data["text"], text_data["word"])
    sentences = text_reader.send_matching_sentences()
    await message.answer(sentences)
    await state.clear()

