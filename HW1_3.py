from typing import Iterable

from HW1_1 import Product, product1, product2
from HW1_2 import Buyer, buyer1


class Order:
    products = []
    buyer = None

    def __init__(self, products: Iterable[Product], buyer: Buyer):
        self.products, self.buyer = products, buyer

    def __str__(self):
        return f'Заказ - {self.buyer.first_name}'

order = Order([product1, product2], buyer1)
if __name__ == '__main__':
    print(order)