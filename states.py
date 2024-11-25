from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    name = State()
    code = State()


class Send_IT(StatesGroup):
    cab = State()
    opis = State()


class Send_Xoz(StatesGroup):
    cab = State()
    opis = State()
