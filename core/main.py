import telebot
import os

API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['text'])
def send_message(message):
    bot.send_message(message.chat.id,'this is a text')

bot.infinity_polling()