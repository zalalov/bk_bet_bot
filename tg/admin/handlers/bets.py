import config
from tg.decorators import is_user_admin, is_admin_mode
from tg.admin.markup import (
    markup_main,
    markup_bets,
    markup_back,
)
from tg.admin.markup import (
    BUTTON_BETS,
    BUTTON_BET_LIST,
    BUTTON_BET_ADD,
)
from tg.admin.utils import parse_bets
from tg.bot import bot

conf = config.get_config()


@bot.message_handler(func=lambda m: m.text == BUTTON_BETS)
@is_admin_mode
@is_user_admin
def bets(message):
    bot.send_message(message.chat.id, 'BETS HANDLER', reply_markup=markup_bets())


@bot.message_handler(func=lambda m: m.text == BUTTON_BET_LIST)
@is_admin_mode
@is_user_admin
def bet_list(message):
    bot.send_message(message.chat.id, 'BET LIST HANDLER', reply_markup=markup_back())


@bot.message_handler(func=lambda m: m.text == BUTTON_BET_ADD)
@is_admin_mode
@is_user_admin
def bet_add(message):
    bot.send_message(
        message.chat.id,
        'Введите ставки разделяя их двумя переводами строки:',
        # reply_markup=markup_save_or_cancel()
    )
    bot.register_next_step_handler(message, bet_add_handler)


def bet_add_handler(message):
    bets = parse_bets(message.text)
    response = '\n'.join(['{content}\n-------------'.format(content=bet['content']) for bet in bets])

    bot.send_message(
        chat_id=message.chat.id,
        text=response,
        reply_markup=markup_main(),
        parse_mode='markdown'
    )
