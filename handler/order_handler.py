import json
from dac.orders_csv import Orders
from dac.products_csv import Products


def handle_callback(bot, callback):
    callback_data = json.loads(callback.data)
    product_id = int(callback_data.get('id', '-1'))
    product_price = float(callback_data.get('price', '-1'))

    if product_id != -1:
        order = {
            'product_id': product_id,
            'quantity': 1,
            'price': product_price }

        Orders(Products()).insert(callback.from_user, order)
        bot.send_message(callback.message.chat.id, f"Спасибо за Ваш заказ!\nСпециалист свяжется с Вами в ближайшее время...")
    else:
        bot.send_message(callback.message.chat.id, f"Что-то пошло не так!\nМы устраним неполадку в ближайшее время...")
