import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from config import TOKEN
from handler import router
from fromUser.sendApplication import sendApplication
from fromUser.getApplications import getApplications
from fromTec.getApplicationsTec import getApplicationsTec
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import states as st
import datetime
import sql
from keyboard import *


bot = Bot(TOKEN)
dp = Dispatcher()


async def run_bot():
    dp.include_router(router)
    dp.include_router(sendApplication)
    dp.include_router(getApplications)
    dp.include_router(getApplicationsTec)

    await dp.start_polling(bot)


@dp.message(st.Send_Xoz.opis)
async def request_four(mes: Message, state: FSMContext):
    await state.update_data(opis=mes.text)
    data = await state.get_data()
    username = sql.getname(mes.from_user.id)
    a = sql.send_application(username[0][0], data["cab"], data["opis"], "Xoz", str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    await mes.answer("Заявка отправлена!\n"
                     f"Имя - {username[0][0].replace('_', ' ')}\n"
                     f"Кабинет - {data['cab']}\n"
                     f"Описание - {data['opis']}\n"
                     f"Отдел - Хоз. отдел\n"
                     f"Время - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                     f"Статус - Отправлена\n"
                     f"Номер заявки - {a+1}", reply_markup=delete_application_1)

    mas = sql.get_otdel("Xoz")
    for i in range(len(mas)):
        await bot.send_message(mas[i][0], "Пришла заявка", reply_markup=but_osn_tec)

    await state.clear()


@dp.message(st.Send_IT.opis)
async def request_four(mes: Message, state: FSMContext):
    await state.update_data(opis=mes.text)
    data = await state.get_data()
    username = sql.getname(mes.from_user.id)
    a = sql.send_application(username[0][0], data["cab"], data["opis"], "IT", str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    await mes.answer("Заявка отправлена!\n"
                     f"Имя - {username[0][0].replace('_', ' ')}\n"
                     f"Кабинет - {data['cab']}\n"
                     f"Описание - {data['opis']}\n"
                     f"Отдел - IT - отдел\n"
                     f"Время - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                     f"Статус - Отправлена\n"
                     f"Номер заявки - {a+1}", reply_markup=delete_application_1)

    mas = sql.get_otdel("IT")
    for i in range(len(mas)):
        await bot.send_message(mas[i][0], "Пришла заявка", reply_markup=but_osn_tec)

    await state.clear()


@dp.callback_query(F.data == "select_application")
async def select_application(cb: CallbackQuery):
    await cb.answer()
    num = int(str(cb.message.text).split(" ")[-1])-1
    sql.select(num)
    await cb.message.delete()
    await cb.message.answer(f"Заявка под номером {num+1} выбрана", reply_markup=but_osn_tec)
    # Найти заявку по id и вывести, добавить replay_markup = but_ok
    id_user = sql.get_id(num)
    await bot.send_message(id_user, "Ваша заявка выполняется!", reply_markup=but_osn)


@dp.callback_query(F.data == "delete_application_tec")
async def delete_application_tec(cb: CallbackQuery):
    await cb.answer()
    num = int(str(cb.message.text).split(" ")[-1]) - 1
    id_user = sql.get_id(num)
    await bot.send_message(id_user, "Ваша заявка отменена!", reply_markup=but_osn)

    sql.delete_application_user(num)
    await cb.message.delete()
    await cb.message.answer(f"Заявка под номером {num + 1} удалена", reply_markup=but_osn_tec)


@dp.callback_query(F.data == "but_ok")
async def but_ok(cb: CallbackQuery):
    await cb.answer()
    num = int(str(cb.message.text).split(" ")[-1]) - 1
    id_user = sql.get_id(num)[0][0]
    await bot.send_message(id_user, "Ваша заявка выполнена!", reply_markup=but_osn)

    sql.ok_application(num)
    await cb.message.delete()
    await cb.message.answer(f"Заявка под номером {num + 1} выполнена", reply_markup=but_osn_tec)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Удалить после разработки
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        print("EXIT")
