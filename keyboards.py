from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Записаться")],
        [KeyboardButton(text="💈 Прайс")]
    ],
    resize_keyboard=True
)

time_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="12:00",
                callback_data="12:00"
            ),
            InlineKeyboardButton(
                text="14:00",
                callback_data="14:00"
            )
        ],
        [
            InlineKeyboardButton(
                text="16:00",
                callback_data="16:00"
            ),
            InlineKeyboardButton(
                text="18:00",
                callback_data="18:00"
            )
        ]
    ]
)

service_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💇 Стрижка",
                callback_data="Стрижка"
            )
        ],
        [
            InlineKeyboardButton(
                text="🧔 Борода",
                callback_data="Борода"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔥 Комплекс",
                callback_data="Комплекс"
            )
        ]
    ]
)
cancel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="❌ Отменить запись",
                callback_data="cancel_booking"
            )
        ]
    ]
)