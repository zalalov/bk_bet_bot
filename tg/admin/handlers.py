import config
from tg.admin.markup import markup_main
from tg.bot import bot

conf = config.get_config()


@bot.message_handler(func=lambda message: conf.is_admin_mode)
@bot.message_handler(func=lambda message: conf.is_user_admin(message.chat.id))
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.from_user.username)
    bot.send_message(message.chat.id, 'Выбери действие:', reply_markup=markup_main())
