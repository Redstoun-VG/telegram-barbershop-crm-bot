from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from config import ADMIN_ID

from database import get_clients, delete_client

router = Router()

@router.message(Command("clients"))
async def show_clients(message: Message):

    if message.from_user.id != ADMIN_ID:

        await message.answer(
            "❌ У вас нет доступа"
        )

        return    

    

    clients = get_clients()

    if not clients:
        await message.answer("Клиентов пока нет")
        return

    text = "📋 Список клиентов:\n\n"

    for client in clients:

        text += (
            f"🆔 ID: {client[0]}\n"
            f"🧑 {client[1]}\n"
            f"📞 {client[2]}\n"
            f"💈 {client[3]}\n"
            f"⏰ {client[4]}\n\n"
        )

    await message.answer(text)

@router.message(Command("delete"))
async def remove_client(message: Message):

    if message.from_user.id != ADMIN_ID:

        await message.answer(
            "❌ У вас нет доступа"
        )

        return    

    try:

        client_id = int(
            message.text.split()[1]
        )

        delete_client(client_id)

        await message.answer(
            f"✅ Клиент {client_id} удалён"
        )

    except:

        await message.answer(
            "❌ Используйте: /delete ID"
        )