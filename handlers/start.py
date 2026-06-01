from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import keyboard

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в барбершоп 😎",
        reply_markup=keyboard
    )