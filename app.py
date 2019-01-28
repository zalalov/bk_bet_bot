from tg.admin.handlers import (
    common,
    bets,
    users
)
import tg.user.handlers
from tg.bot import bot


if __name__ == '__main__':
    bot.polling()