import os
import pandas as pd


class Orders:
    def __init__(self):
        self.csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/orders.csv'))

    def insert(self, order:dict):
        df = pd.DataFrame([order])
        df.to_csv(self.csv_path, mode='a', header=False, index=False)

    def get_products_reserved(self, product_id:int):
        orders_df = pd.read_csv(self.csv_path)
        reserved_df = orders_df.loc[(orders_df['product_id']==product_id) & (~orders_df['status'].str.lower().isin(['done','+','готово','закрыт','выполнено']))]
        
        return len(reserved_df.index)
