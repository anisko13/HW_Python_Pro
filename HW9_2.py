func_lst = []
def count_decorator(f):
    func_lst.append(f)
    def wrapper(*args):
        f(*args)
    return wrapper

@count_decorator
def print_hello():
    print('hello')
    

@count_decorator
def print_bye():
    print('bye')

if __name__ == '__main__':
    print(func_lst)
