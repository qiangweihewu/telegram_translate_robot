import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from translate import get_translate_results

# 机器人的TOKEN填在这里
TOKEN = ''

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_all(message):
    cid = message.chat.id
    bot.send_message(cid, get_translate_results(message.text))
    print(message.text)


bot.polling()
