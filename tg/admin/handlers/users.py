import config
from tg.decorators import is_user_admin, is_admin_mode
from tg.admin.markup import (
    markup_users,
    markup_back,
    markup_main
)
from tg.admin.markup import (
    BUTTON_USERS,
    BUTTON_USER_ADD,
    BUTTON_USER_LIST,
)
from tg.admin.utils import parse_users
from tg.bot import bot

conf = config.get_config()


@bot.message_handler(func=lambda m: m.text == BUTTON_USERS)
@is_admin_mode
@is_user_admin
def users(message):
    bot.send_message(message.chat.id, 'USERS HANDLER', reply_markup=markup_users())


@bot.message_handler(func=lambda m: m.text == BUTTON_USER_LIST)
@is_admin_mode
@is_user_admin
def user_list(message):
    bot.send_message(message.chat.id, 'USER LIST HANDLER', reply_markup=markup_back())


@bot.message_handler(func=lambda m: m.text == BUTTON_USER_ADD)
@is_admin_mode
@is_user_admin
def bet_add(message):
    bot.send_message(
        message.chat.id,
        'Введите имена пользователей разделяя их переводами строки',
        # reply_markup=markup_save_or_cancel()
    )
    bot.register_next_step_handler(message, user_add_handler)



def user_add_handler(message):
    users = parse_users(message.text)

    response = '\n'.join(['{i}. {content}\n'.format(i=i, content=user) for i, user in enumerate(users)])

    bot.send_message(
        chat_id=message.chat.id,
        text=response,
        reply_markup=markup_main(),
        parse_mode='markdown'
    )