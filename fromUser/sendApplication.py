from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboard import *
import emoji
import sql
import states as st
import datetime


sendApplication = Router()


@sendApplication.callback_query(F.data == "send")
async def request_one(cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text(text="Отправка заявки!", reply_markup=None)
    await cb.message.answer(text=f"Выберете отдел{emoji.emojize(':backhand_index_pointing_down:')}",
                            reply_markup=but_otdel)


# IT - отдел


@sendApplication.callback_query(F.data == "check_send_it")
async def request_two(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await cb.message.edit_text("Вы выбрали IT - отдел", reply_markup=None)
    await cb.message.answer("Напишите номер кабинета", reply_markup=None)
    await state.set_state(st.Send_IT().cab)


@sendApplication.message(st.Send_IT.cab)
async def request_three(mes: Message, state: FSMContext):
    await state.update_data(cab=mes.text)
    await mes.answer("Опишите проблему", reply_markup=None)
    await state.set_state(st.Send_IT.opis)


# Xoz отдел


@sendApplication.callback_query(F.data == "check_send_xoz")
async def request_two(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await cb.message.edit_text("Вы выбрали Хоз. отдел", reply_markup=None)
    await cb.message.answer("Напишите номер кабинета", reply_markup=None)
    await state.set_state(st.Send_Xoz().cab)


@sendApplication.message(st.Send_Xoz.cab)
async def request_three(mes: Message, state: FSMContext):
    await state.update_data(cab=mes.text)
    await mes.answer("Опишите проблему", reply_markup=None)
    await state.set_state(st.Send_Xoz.opis)



