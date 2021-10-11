import os
import pandas as pd


class Products:
    def __init__(self, orders_dac=None):
        self.csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/products.csv'))
        self.orders_dac = orders_dac
        if orders_dac is not None:
            self.orders_dac.products_dac = self

    def get_list(self, limit:int=-1):
        product_df = pd.read_csv(self.csv_path)

        # todo: do it via column operation
        product_df['num_reserved'] = [self.orders_dac.get_products_reserved(product_id) for product_id in product_df.id]
        product_df['num_available'] = product_df.num_total - product_df.num_reserved
        product_df = product_df.loc[product_df.num_available > 0]

        return product_df.head(limit) if limit > 0 else product_df
    
    def get_product_name(self, product_id:int):
        product_df = pd.read_csv(self.csv_path)
        products = product_df.loc[product_df['id']==product_id]
        
        if products is None or len(products.index) == 0:
            return None

        return products.name.iloc[0]
