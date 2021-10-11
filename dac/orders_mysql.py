import os
import mysql.connector

class Orders:
    def __init__(self, products_dac=None):
        self.connection_string = eval(os.getenv('CONNECTION_STRING'))

        self.products_dac = products_dac
        if products_dac is not None:
            self.products_dac.orders_dac = self

    def insert(self, user, order:dict):
        connection = mysql.connector.connect(**self.connection_string)
        # TBD
        # connection.cursor().execute()

    def get_products_reserved(self, product_id:int):
        # TBD
        pass
