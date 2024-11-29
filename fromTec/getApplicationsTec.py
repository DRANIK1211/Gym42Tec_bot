from aiogram import F, Router
from aiogram.types import CallbackQuery
from keyboard import *
import sql

getApplicationsTec = Router()


@getApplicationsTec.callback_query(F.data == "get_application_tec")
async def get_applications_tec(cb: CallbackQuery):
    await cb.answer()
    #  Исправить просмотр заявок, выходили только "Отправлена", нужно добавить в вывод "Выполняется"
    otdel = sql.get_otdel_tec(cb.from_user.id)[0][0]
    mas = sql.get_application_tec(otdel)
    if not mas:
        await cb.message.answer("Новых заявок нет")
        return
    await cb.message.edit_text("Просмотр заявок", reply_markup=but_osn_tec)
    for i in range(len(mas)):
        if mas[i][-1] == "Отправлена":
            a = but_tec
        if mas[i][-1] == "Выполняется":
            a = but_okk
        await cb.message.answer(
            f"ФИО - {mas[i][1].replace('_', ' ')}\n"
            f"Номер кабинета - {mas[i][2]}\n"
            f"Описание:\n{mas[i][3]}\n"
            f"Время отправки - {mas[i][5]}\n"
            f"Статус - {mas[i][-1]}\n"
            f"Номер заявки - {mas[i][0] + 1}",
            reply_markup=a)
