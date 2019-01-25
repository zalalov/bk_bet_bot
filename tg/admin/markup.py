from telebot import types


BUTTON_USERS = '👬 Пользователи'
BUTTON_BETS = '✍️ Cтавки'

BUTTON_USER_LIST = '📜 Список пользователей'
BUTTON_USER_ADD = '➕ Добавить пользователей'

BUTTON_BET_LIST = '📜 Список ставок'
BUTTON_BET_ADD = '➕ Добавить ставки'
BUTTON_BET_SAVE = '💾 Сохранить ставки'

BUTTON_BACK = '🔙 Назад'
BUTTON_CLEAR_ALL = '🚽 Очистить все'
BUTTON_CANCEL = '❌ Отмена'

def markup_main():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(
        BUTTON_USERS,
        BUTTON_BETS,
        BUTTON_CLEAR_ALL
    )

    return markup

def markup_back():
    markup = types.ReplyKeyboardMarkup()
    markup.add(
        BUTTON_BACK
    )

    return markup

def markup_users():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(
        BUTTON_USER_LIST,
        BUTTON_USER_ADD
    )

    return markup

def markup_bets():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(
        BUTTON_BET_LIST,
        BUTTON_BET_ADD
    )

    return markup

def markup_save_or_cancel():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(
        BUTTON_BET_SAVE,
        BUTTON_CANCEL
    )

    return markup
