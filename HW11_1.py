class Descriptor:
    def __init__(self, n):
        self.n = n

    def __set__(self, instance, value):
        raise AttributeError("field is read-only")

    def __get__(self, instance_self, instance_class):
        return self.n


class Cat:
    def __init__(self, name):
        self.name = name

    voice = Descriptor('mew')


cat = Cat('murzik')
cat.voice = 'hello'
print(cat.voice)
