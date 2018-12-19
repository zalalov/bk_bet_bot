import config
from tg.decorators import is_user_admin, is_admin_mode
from tg.admin.markup import (
    markup_main,
    markup_bets,
    markup_users,
    markup_back
)
from tg.admin.markup import (
    BUTTON_USERS,
    BUTTON_BETS,
    BUTTON_USER_ADD,
    BUTTON_USER_LIST,
    BUTTON_BET_LIST,
    BUTTON_BET_ADD,
    BUTTON_BACK,
)
from tg.bot import bot

conf = config.get_config()


@bot.message_handler(commands=['start'])
@is_admin_mode
@is_user_admin
def main_menu(message):
    bot.send_message(message.chat.id, 'Выбери действие:', reply_markup=markup_main())


@bot.message_handler(func=lambda m: m.text == BUTTON_USERS)
@is_admin_mode
@is_user_admin
def users(message):
    bot.send_message(message.chat.id, 'USERS HANDLER', reply_markup=markup_users())


@bot.message_handler(func=lambda m: m.text == BUTTON_USER_LIST)
@is_admin_mode
@is_user_admin
def users(message):
    bot.send_message(message.chat.id, 'USER LIST HANDLER', reply_markup=markup_back())


@bot.message_handler(func=lambda m: m.text == BUTTON_BETS)
@is_admin_mode
@is_user_admin
def users(message):
    bot.send_message(message.chat.id, 'BETS HANDLER', reply_markup=markup_bets())


@bot.message_handler(func=lambda m: m.text == BUTTON_BET_LIST)
@is_admin_mode
@is_user_admin
def users(message):
    bot.send_message(message.chat.id, 'BET LIST HANDLER', reply_markup=markup_back())


@bot.message_handler(func=lambda m: m.text == BUTTON_BACK)
@is_admin_mode
@is_user_admin
def users(message):
    main_menu(message)
