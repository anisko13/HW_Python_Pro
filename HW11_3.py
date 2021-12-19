import time

class Descriptor:
    def __init__(self, n):
        self.n = n

    def __set__(self, instance, value):
        with open('changevalue.txt', 'w') as file:
            file.write(str(time.time()) + ' ' + str(value))
        self.n = value

    def __get__(self, instance_self, instance_class):
        return self.n


class Cat:

    age = Descriptor(0)


cat = Cat()
cat.age = 2
print(cat.age)