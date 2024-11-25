from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from keyboard import *
import emoji
import sql
import states as st
import config as cd

router = Router()


@router.message(CommandStart())
async def start(mes: Message):
    if not sql.search(mes.from_user.id):
        await mes.answer(f"Здравствуйте, это бот Гимназии №42 г. Барнаула,"
                         f" предназначенный для приёма заявок на ремонт оборудования\n"
                         f"Пожалуйста, выберете действие {emoji.emojize(':backhand_index_pointing_down:')}",
                         reply_markup=start_buttons)
    else:
        otdel = sql.get_otdel_tec(mes.from_user.id)
        match otdel:
            case "User":
                a = but_osn
            case "IT":
                a = but_osn_tec
            case "Xoz":
                a = but_osn_tec
            case "Admin":
                a = admin_but
        await mes.answer(f"С возвращением, это бот Гимназии №42 г. Барнаула,"
                         f" предназначенный для приёма заявок на ремонт оборудования\n"
                         f"Пожалуйста, выберете действие {emoji.emojize(':backhand_index_pointing_down:')}",
                         reply_markup=a)


@router.callback_query(F.data == "reg_but")
async def register_one(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await cb.message.edit_text("Регистрация!\nВведите ФИО, например:\nИванов Иван Иванович", reply_markup=None)
    await state.set_state(st.Register.name)


@router.message(st.Register.name)
async def register_two(mes: Message, state: FSMContext):
    await state.update_data(name=mes.text.lower().replace(" ", "_"))
    await mes.answer("Регистрация!\nВведите ваше кодовое слово")
    await state.set_state(st.Register.code)


@router.message(st.Register.code)
async def register_three(mes: Message, state: FSMContext):
    await state.update_data(code=mes.text)
    data = await state.get_data()
    if data["code"] == cd.CODE_1:
        sql.register(int(mes.from_user.id), data["name"], "User")
        await mes.answer(f"Вы успешно зарегистрированы как Пользователь!\n"
                         f"Пожалуйста, выберете действие{emoji.emojize(':backhand_index_pointing_down:')}",
                         reply_markup=but_osn)
    elif data["code"] == cd.CODE_2:
        sql.register(int(mes.from_user.id), data["name"], "IT")
        await mes.answer(f"Вы успешно зарегистрированы в IT отдел!\n"
                         f"Пожалуйста, выберете действие{emoji.emojize(':backhand_index_pointing_down:')}",
                         reply_markup=but_osn_tec)
    elif data["code"] == cd.CODE_3:
        sql.register(int(mes.from_user.id), data["name"], "Xoz")
        await mes.answer(f"Вы успешно зарегистрированы в хоз. отдел!\n"
                         f"Пожалуйста, выберете действие{emoji.emojize(':backhand_index_pointing_down:')}",
                         reply_markup=but_osn_tec)
    elif data["code"] == cd.CODE_4:
        sql.register(int(mes.from_user.id), data["name"], "Admin")
        await mes.answer(f"Вы успешно зарегистрированы как Админ!\n"
                         f"Пожалуйста, выберете действие{emoji.emojize(':backhand_index_pointing_down:')}",
                         reply_markup=admin_but)
    else:
        await mes.answer("Неизвестная ошибка\n"
                         f"Пожалуйста, выберете действие {emoji.emojize(':backhand_index_pointing_down:')}",
                         reply_markup=start_buttons)
    await state.clear()


# delete application
@router.callback_query(F.data == "delete_application")
async def delete_application(cb: CallbackQuery):
    await cb.answer()
    num = int(str(cb.message.text).split(" ")[-1])-1
    await cb.message.answer(f"Заявка под номером {num + 1} была удалена!", reply_markup=but_osn)
    sql.delete_application_user(num)
    await cb.message.delete()

