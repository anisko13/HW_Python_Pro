def custom_func_range(first, count, func):
    index = first
    step = 0
    while step < count:
        index = func(index)
        yield index
        step += 1


def add(number):
    return number + 1


if __name__ == '__main__':
    print(list(custom_func_range(3, 5, add)))
