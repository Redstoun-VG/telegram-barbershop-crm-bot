from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from datetime import datetime, timedelta
from database import is_time_taken

def get_time_keyboard(date):

    times = [
        "12:00",
        "14:00",
        "16:00",
        "18:00"
    ]

    keyboard = []

    for time in times:

        if not is_time_taken(date, time):

            keyboard.append(
                [
                    InlineKeyboardButton(
                        text=time,
                        callback_data=time
                    )
                ]
            )

    if not keyboard:

        keyboard.append(
            [
                InlineKeyboardButton(
                    text="❌ Нет свободного времени",
                    callback_data="no_time"
                )
            ]
        )

    return InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Записаться")],
        [
            KeyboardButton(text="👤 Мои записи"),
            KeyboardButton(text="💈 Услуги")
        ],
        [
            KeyboardButton(text="ℹ️ Инфо"),
            KeyboardButton(text="💬 Поддержка")
        ]
    ],
    resize_keyboard=True
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


def get_date_keyboard():

    keyboard = []

    today = datetime.now()

    for i in range(14):

        date = today + timedelta(days=i)

        formatted_date = date.strftime("%d.%m")

        keyboard.append(
            [
                InlineKeyboardButton(
                    text=f"📅 {formatted_date}",
                    callback_data=formatted_date
                )
            ]
        )

    return InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )



admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📊 Статистика"
            )
        ],
        [
            KeyboardButton(
                text="📅 Сегодня"
            ),
            KeyboardButton(
                text="📆 Неделя"
            )
        ],
        [
            KeyboardButton(
                text="👥 Клиенты"
            )
        ]
    ],
    resize_keyboard=True
)
