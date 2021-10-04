import telebot
import json


def create_order_markup(message, row):
    data = json.dumps({"op": "order", "id": row.id, 'price': str(row.price)})
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text=f'Заказать ({row.price} руб)', callback_data=data))

    return markup

def create_menu_markup(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.one_time_keyboard = True
    price_btn = telebot.types.KeyboardButton('Весь прайс')
    order_status_btn = telebot.types.KeyboardButton('Статус заказа')
    markup.row(price_btn, order_status_btn)

    return markup
