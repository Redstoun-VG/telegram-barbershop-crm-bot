from aiogram import Router, F, Bot
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.fsm.context import FSMContext
from database import get_user_bookings



from database import (
    save_client,
    get_user_bookings,
    is_time_taken
)
from keyboards import (
    service_keyboard,
    get_date_keyboard,
    get_time_keyboard
)
from states import Order
from config import ADMIN_ID

router = Router()

# ---------- ПРАЙС ----------

@router.message(F.text == "💈 Услуги")
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
        "📅 Выберите дату:",
        reply_markup=get_date_keyboard()
    )

    await state.set_state(Order.date)

    await callback.answer()

@router.callback_query(Order.date)
async def get_date(
    callback: CallbackQuery,
    state: FSMContext
):

    await state.update_data(date=callback.data)

    await callback.message.answer(
        "⏰ Выберите время:",
        reply_markup=get_time_keyboard(callback.data)
    )

    await state.set_state(Order.time)

    await callback.answer() 
    
@router.callback_query(Order.time)
async def get_time(
    callback: CallbackQuery,
    state: FSMContext,
    bot: Bot
):

    data = await state.get_data()

    date = data["date"]
    time = callback.data

    if is_time_taken(date, time):

        await callback.message.answer(
            "❌ Это время уже занято"
        )

        await callback.answer()

        return

    save_client(
        callback.from_user.id,
        data["name"],
        data["phone"],
        data["service"],
        date,
        time
    )

    await callback.message.answer(
        f"✅ Вы записаны!\n\n"
        f"📅 Дата: {date}\n"
        f"⏰ Время: {time}"
    )

    await bot.send_message(
        ADMIN_ID,
        f"📢 Новая запись!\n\n"
        f"🧑 Имя: {data['name']}\n"
        f"📞 Телефон: {data['phone']}\n"
        f"💈 Услуга: {data['service']}\n"
        f"📅 Дата: {date}\n"
        f"⏰ Время: {time}"
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
    
     

@router.message(F.text == "👤 Мои записи")
async def my_bookings(message: Message):

    bookings = get_user_bookings(
        message.from_user.id
    )

    if not bookings:

        await message.answer(
            "❌ У вас пока нет записей"
        )

        return

    for booking in bookings:

        booking_id = booking[0]

        cancel_booking_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="❌ Отменить",
                        callback_data=f"cancel_{booking_id}"
                    )
                ]
            ]
        )

        await message.answer(
    f"💈 {booking[4]}\n"
    f"📅 {booking[5]}\n"
    f"⏰ {booking[6]}",
    reply_markup=cancel_booking_keyboard
)