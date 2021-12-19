def custom_range(first, last, step=1):
    index = first
    while index < last:
        yield index
        index += step


if __name__ == '__main__':
    print(list(custom_range(3, 23, 7)))