from aiogram.fsm.state import State, StatesGroup

class Order(StatesGroup):
    name = State()
    phone = State()
    service = State()
    date = State()
    time = State()