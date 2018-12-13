import telebot
from config import get_config

config = get_config()
bot = telebot.TeleBot(config.TG_BOT_TOKEN)
