import os
import pandas as pd
from dac.orders_csv import Orders


class Products:
    def __init__(self):
        self.csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/products.csv'))

    def get_list(self, limit:int=-1):
        product_df = pd.read_csv(self.csv_path)
        orders = Orders()

        # todo: do it via column operation
        product_df['num_reserved'] = [orders.get_products_reserved(product_id) for product_id in product_df.id]
        product_df['num_available'] = product_df.num_total - product_df.num_reserved
        product_df = product_df.loc[product_df.num_available > 0]

        return product_df.head(limit) if limit > 0 else product_df
    
    def get_product_name(self, product_id:int):
        product_df = pd.read_csv(self.csv_path)
        products = product_df.loc[product_df['id']==product_id]
        
        if products is None or len(products.index) == 0:
            return None

        return products.name.iloc[0]
