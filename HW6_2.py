from HW1_1 import Product, product1, product2
from HW1_2 import Buyer, buyer1
from HW1_3 import Order as OldOrder

class OrderIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index = self.index + 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self

class Order(OldOrder):
    def __iter__(self):
        return OrderIterator(self.products)

    def __getitem__(self, index):
        return self.products[index]

if __name__ == '__main__':
    order = Order([product1, product2], buyer1)
    for product in order:
        print(product)
    print(order[0])