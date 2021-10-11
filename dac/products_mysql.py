import os
import pandas as pd
import mysql.connector


class Products:
    def __init__(self, orders_dac=None):
        self.connection_string = eval(os.getenv('CONNECTION_STRING'))
        self.orders_dac = orders_dac
        if orders_dac is not None:
            self.orders_dac.products_dac = self

    def get_list(self, limit:int=-1):
        product_df = self.__get_product_df()

        # todo: do it via column operation
        product_df['num_reserved'] = [self.orders_dac.get_products_reserved(product_id) for product_id in product_df.id]
        product_df['num_available'] = product_df.num_total - product_df.num_reserved
        product_df = product_df.loc[product_df.num_available > 0]

        return product_df.head(limit) if limit > 0 else product_df
    
    def get_product_name(self, product_id:int):
        connection = mysql.connector.connect(**self.connection_string)

        try:
            df = pd.read_sql_query(f'select name from products WHERE id={product_id}', connection)
            if len(df.index) > 0:
                return df.at[0, 'name']
        finally:
            connection.close()
        
        return ''

    def __get_product_df(self):
        connection = mysql.connector.connect(**self.connection_string)

        try:
            return pd.read_sql_query('select * from products', connection)
        finally:
            connection.close()
