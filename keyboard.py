from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

but_reg = InlineKeyboardButton(text="Зарегистрироваться", callback_data="reg_but")

start_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [but_reg]
    ]
)

but_osn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Создать заявку", callback_data="send")],
        [InlineKeyboardButton(text="Посмотреть заявки", callback_data="get_application")]
    ]
)

but_osn_tec = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть заявки", callback_data="get_application_tec")]
    ]
)

but_tec = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Взять заявку на себя", callback_data="select_application")],
        [InlineKeyboardButton(text="Отменить заявку", callback_data="delete_application_tec")]
    ]
)


but_ok = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Заявка выполнена", callback_data="but_ok")]
    ]
)


admin_but = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Удалить пользователя", callback_data="delete_user")],
        [InlineKeyboardButton(text="Создать отчёт", callback_data="create_report")]
    ]
)

but_otdel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="IT - отдел", callback_data="check_send_it")],
        [InlineKeyboardButton(text="Хоз. отдел", callback_data="check_send_xoz")]
    ]
)

delete_application = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Удалить заявку", callback_data="delete_application")]
    ]
)

delete_application_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Удалить заявку", callback_data="delete_application")],
        [InlineKeyboardButton(text="Оставить заявку", callback_data="send")],
        [InlineKeyboardButton(text="Посмотреть заявки", callback_data="get_application")]
    ]
)