# main.py
from telebot import TeleBot
from handlers import start, analyze, crypto
import config

bot = TeleBot(config.BOT_TOKEN)

# ثبت هندلرها
start.register(bot)
analyze.register(bot)
crypto.register(bot)

# اجرای ربات
bot.infinity_polling()
