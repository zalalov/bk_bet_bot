from telebot import types


BUTTON_USERS = '👬 Пользователи'
BUTTON_ADD_BET = '✍️ Добавить ставку'
BUTTON_CLEAR_ALL = '🚽 Очистить все'

def markup_main():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(
        BUTTON_USERS,
        BUTTON_ADD_BET,
        BUTTON_CLEAR_ALL
    )

    return markup

