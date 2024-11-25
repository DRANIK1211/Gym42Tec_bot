from aiogram import F, Router
from aiogram.types import CallbackQuery
from keyboard import *
import sql

getApplications = Router()


@getApplications.callback_query(F.data == "get_application")
async def get_application(cb: CallbackQuery):
    await cb.answer()
    #  Исправить просмотр заявок, выходили только "Отправлена", нужно добавить в вывод "Выполняется"
    mas = sql.get_application(cb.from_user.id)

    if not mas:  # Проверяем, есть ли заявки
        await cb.message.answer("У вас нет заявок.")
        return
    await cb.message.answer(
        "Просмотр заявок", reply_markup=but_osn
    )
    for i in range(0, len(mas)):
        if mas[i][4] == 'IT':
            a = "IT - отдел"
        else:
            a = "Хоз. отдел"

        if mas[i][-1] == "Отправлено":
            b = delete_application
        else:
            b = None
        await cb.message.answer(
            f"Заявка в {a}\n"
            f"ФИО - {mas[i][1].replace('_', ' ')}\n"
            f"Кабинет - {mas[i][2]}\n"
            f"Описание проблемы:\n{mas[i][3]}\n"
            f"Дата - {mas[i][5]}\n"
            f"Статус - {mas[i][6]}\n"
            f"Номер заявки - {mas[i][0] + 1}",
            reply_markup=b)
