from functools import wraps


def save_to_file(f):
    @wraps(f)
    def wrapper(*args):
        # with open(f'{f.__class__.__name__}.txt', 'w') as file:
        with open(f'Cat.txt', 'w') as file:
            file.write(f(*args))
        return f(*args)

    return wrapper


class Cat:

    @save_to_file
    def __str__(self) -> str:
        return 'new Cat'

cat = Cat()
print(cat)
