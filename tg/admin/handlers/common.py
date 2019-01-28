import config
from tg.decorators import is_user_admin, is_admin_mode
from tg.admin.markup import (
    markup_main,
    markup_bets,
    markup_users,
    markup_back,
    markup_save_or_cancel
)
from tg.admin.markup import (
    BUTTON_USERS,
    BUTTON_BETS,
    BUTTON_USER_ADD,
    BUTTON_USER_LIST,
    BUTTON_BET_LIST,
    BUTTON_BET_ADD,
    BUTTON_BACK,
    BUTTON_BET_SAVE,
    BUTTON_CANCEL
)
from tg.admin.utils import parse_bets
from tg.bot import bot

conf = config.get_config()


@bot.message_handler(func=lambda m: m.text == BUTTON_BACK)
@is_admin_mode
@is_user_admin
def back(message):
    main_menu(message)


@bot.message_handler(commands=['start'])
@is_admin_mode
@is_user_admin
def main_menu(message):
    bot.send_message(message.chat.id, 'Выбери действие:', reply_markup=markup_main())
