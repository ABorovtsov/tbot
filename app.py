import os
from dotenv import load_dotenv
import telebot
from request_filters import is_hello_request, is_order_callback
import handler.hello_handler
import handler.order_handler


load_dotenv()
bot = telebot.TeleBot(os.getenv('API_KEY'))


@bot.message_handler(func=is_hello_request)
def home(message):
    handler.hello_handler.handle(bot, message)


@bot.callback_query_handler(func=is_order_callback)
def handle_query(callback):
    handler.order_handler.handle_callback(bot, callback)


bot.polling()