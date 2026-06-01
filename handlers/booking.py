from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from database import save_client
from keyboards import (
    time_keyboard,
    service_keyboard,
    cancel_keyboard
)
from states import Order
from config import ADMIN_ID

router = Router()

# ---------- ПРАЙС ----------

@router.message(F.text == "💈 Прайс")
async def price(message: Message):
    await message.answer(
        "Стрижка — 1500₽\n"
        "Борода — 800₽\n"
        "Комплекс — 2000₽"
    )

# ---------- ЗАПИСЬ ----------

@router.message(F.text == "📅 Записаться")
async def booking_start(message: Message, state: FSMContext):
    await message.answer("Введите ваше имя:")
    await state.set_state(Order.name)

# ---------- ИМЯ ----------

@router.message(Order.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer("Введите ваш номер телефона:")
    await state.set_state(Order.phone)

# ---------- ТЕЛЕФОН ----------

@router.message(Order.phone)
async def get_phone(message: Message, state: FSMContext):

    phone = message.text

    if not phone.isdigit():

        await message.answer(
            "❌ Номер должен содержать только цифры"
        )

        return

    if len(phone) < 10:

        await message.answer(
            "❌ Слишком короткий номер"
        )

        return

    await state.update_data(phone=phone)

    await message.answer(
        "Выберите услугу:",
        reply_markup=service_keyboard
    )

    await state.set_state(Order.service)

# ---------- УСЛУГА ----------

@router.callback_query(Order.service)
async def get_service(
    callback: CallbackQuery,
    state: FSMContext
):

    await state.update_data(service=callback.data)

    await callback.message.answer(
        "Выберите время:",
        reply_markup=time_keyboard
    )

    await state.set_state(Order.time)

    await callback.answer()

# ---------- ВРЕМЯ ----------

@router.callback_query(Order.time)
async def get_time(
    callback: CallbackQuery,
    state: FSMContext,
    bot: Bot
):

    await state.update_data(time=callback.data)

    data = await state.get_data()

    client_id = save_client(
    data["name"],
    data["phone"],
    data["service"],
    data["time"]
)

    cancel_keyboard.inline_keyboard[0][0].callback_data = (
    f"cancel_{client_id}"
)

    await callback.message.answer(
    f"✅ Вы записаны на {data['time']}",
    reply_markup=cancel_keyboard
)

    await bot.send_message(
        ADMIN_ID,
        f"📢 Новая запись!\n\n"
        f"🧑 Имя: {data['name']}\n"
        f"📞 Телефон: {data['phone']}\n"
        f"💈 Услуга: {data['service']}\n"
        f"⏰ Время: {data['time']}"
    )

    await callback.answer()

    await state.clear()


@router.callback_query(F.data.startswith("cancel_"))
async def cancel_booking(callback: CallbackQuery):

    client_id = int(
        callback.data.split("_")[1]
    )

    from database import delete_client

    delete_client(client_id)

    await callback.message.answer(
        "❌ Запись отменена"
    )

    await callback.answer()    