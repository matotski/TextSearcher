from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from keyboard.userkeyboard import get_back_keyboard

router = Router()


class SearchByWord(StatesGroup):
    file = State()
    word = State()


@router.callback_query(StateFilter(None), F.data == "search_file")
async def text_file_reader(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await callback.message.answer("Отлично, отправь мне файл", reply_markup=get_back_keyboard())
    if callback.message.document is not None:
        file_url = await callback.message.bot.get_file(callback.message.document.file_id)
        file = await bot.download(file_url.file_path)
    await callback.answer()
    await state.set_state(SearchByWord.file)


@router.message(SearchByWord.file)
async def get_word(message: Message, state: FSMContext):
    await state.update_data(file = message.document)
    await message.answer("Супер! Теперь отправь мне искомое слово", reply_markup=get_back_keyboard())
    await state.set_state(SearchByWord.word)


# @router.message(SearchByWord.word,F.text)
# async def send_sentences(callback: CallbackQuery, state: FSMContext):
#     await state.update_data(word = callback.message.text)
#     text_data = await state.get_data()
#     text_reader = TextReader(text_data["text"], text_data["word"])
#     sentences = text_reader.send_matching_sentences()
#     await message.answer(sentences)
#     await state.clear()