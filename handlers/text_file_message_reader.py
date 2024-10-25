from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery
from main import bot
from keyboard.userkeyboard import get_back_keyboard

router = Router()

class SearchByWord(StatesGroup):
    text = State()
    word = State()

@router.callback_query(StateFilter(None),F.data == "search_file")
async def message_reader(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Отправь мне файл")
    await callback.message.edit_reply_markup(reply_markup=get_back_keyboard())
    await callback.answer()