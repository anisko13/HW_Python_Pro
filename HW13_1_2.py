import abc

class CheckInt(abc.ABC):
    
    @abc.abstractmethod
    def check_int(self, n):
        return isinstance(n, int)
    

class Subclass(CheckInt):
    def check_int(self, n):
        return isinstance(n, int)

d = Subclass()
print(d.check_int(12))
