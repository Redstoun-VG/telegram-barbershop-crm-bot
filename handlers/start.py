from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import FSInputFile

from keyboards import keyboard

router = Router()

@router.message(CommandStart())
async def start(message: Message):

    photo = FSInputFile("images/banner.png")

    await message.answer_photo(
        photo=photo,
        caption=(
            "💈 Добро пожаловать в Barber CRM Bot\n\n"
            "Твой стиль. Твои правила. 😎\n\n"
            "Выберите действие ниже 👇"
        ),
        reply_markup=keyboard
    )

@router.message(F.text == "ℹ️ Инфо")
async def info(message: Message):

    await message.answer(
        "👨‍💻 Разработчик Telegram ботов\n\n"
        "🔹 CRM системы\n"
        "🔹 Боты записи\n"
        "🔹 AI интеграции\n"
        "🔹 Автоматизация бизнеса\n\n"
        "📩 Связь: @@Redstounn"
    )  
    
@router.message(F.text == "💬 Поддержка")
async def support(message: Message):

    await message.answer(
        "💬 Связь с разработчиком:\n\n"
        "@Redstounn"
    )      