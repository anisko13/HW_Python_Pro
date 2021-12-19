count = 0
def count_decorator(f):
    def wrapper(*args):
        global count
        count += 1
        f(*args)
    return wrapper

@count_decorator
def print_hello():
    print('hello')

if __name__ == '__main__':
    print_hello()
    print_hello()
    print_hello()
    print(count)