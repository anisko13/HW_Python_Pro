class Product:
    price = ''
    description = ''
    size = ''

    def __init__(self, price, description, size):
        self.price = price
        self.description = description
        self.size = size

    def __str__(self):
        return f'Продукт - {self.description}'

product1 = Product(5, 'fluffy', 6)
product2 = Product(4, 'strict', 7)


if __name__ == '__main__':
    print(product1,'\n', product2)
