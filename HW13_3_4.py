import abc

class AbstractValidator(abc.ABC):
    pass
        

class Subclass():
    def check_int(self, n):
        return isinstance(n, int)
    

AbstractValidator.register(Subclass)

d = Subclass()
print(isinstance(d, AbstractValidator))
