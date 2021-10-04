import json
import datetime
from dac.orders_csv import Orders
from dac.products_csv import Products


def handle_callback(bot, callback):
    callback_data = json.loads(callback.data)
    product_id = int(callback_data.get('id', '-1'))
    product_name = callback_data.get('name', 'unknown')
    product_price = int(callback_data.get('price', '-1'))

    if product_id != -1:
        order = {
            'user_name':callback.from_user.full_name,
            'user_id':callback.from_user.id,
            'time': str(datetime.datetime.utcnow()),
            'product_id': product_id,
            'product_name': Products().get_product_name(product_id) if product_name == 'unknown' else product_name,
            'num': 1,
            'price': product_price,
            'status': 'открыт',
            'comment': ''}

        Orders().insert(order)
        bot.send_message(callback.message.chat.id, f"Спасибо за Ваш заказ!\nСпециалист свяжется с Вами в ближайшее время...")
    else:
        bot.send_message(callback.message.chat.id, f"Что-то пошло не так!\nМы устраним неполадку в ближайшее время...")
