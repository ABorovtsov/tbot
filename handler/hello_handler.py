from markup import create_menu_markup, create_order_markup
from dac.products_csv import Products


def handle(bot, message):
    bot.send_message(message.chat.id, f"Привет!", disable_web_page_preview=False, reply_markup=create_menu_markup(message))
    bot.send_message(message.chat.id, f"<b>Популярное у нас:</b>", parse_mode='HTML')

    for index, row in Products().get_list(3).iterrows():
        bot.send_message(message.chat.id, f"{row['name']}")
        if len(row.img_link) > 0:
            bot.send_photo(message.chat.id, photo = row.img_link)
            
        bot.send_message(message.chat.id, f"{row.description}", reply_markup=create_order_markup(message, row))
