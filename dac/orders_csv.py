import os
import pandas as pd
import datetime

class Orders:
    def __init__(self, products_dac=None):
        self.csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/orders.csv'))

        with open(self.csv_path, 'r', encoding='utf-8') as csv:
            line = next(csv)
            self.columns = line.strip().split(',')

        self.products_dac = products_dac
        if products_dac is not None:
            self.products_dac.orders_dac = self

    def insert(self, user, order:dict):
        order['product_name'] = self.products_dac.get_product_name(order['product_id'])
        order['status'] = 'открыт'
        order['comment'] = ''
        order['user_first_name'] = user.first_name
        order['user_last_name'] = user.last_name
        order['user_name'] = user.username
        order['user_id'] = user.id
        order['user_is_bot'] = user.is_bot
        order['time'] = str(datetime.datetime.utcnow())

        df = pd.DataFrame([order])

        df.to_csv(self.csv_path, mode='a', header=False, index=False, columns=self.columns)

    def get_products_reserved(self, product_id:int):
        orders_df = pd.read_csv(self.csv_path)
        reserved_df = orders_df.loc[(orders_df['product_id']==product_id) & (~orders_df['status'].str.lower().isin(['done','+','готово','закрыт','выполнено']))]
        
        return len(reserved_df.index)
