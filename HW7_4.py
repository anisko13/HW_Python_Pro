def cube_range(some_list, target_number):
    index = 2
    while index < target_number:
        yield some_list.append(index * index * index)
        index += 1


if __name__ == '__main__':
    some_list = []
    target_number = 17
    list(cube_range(some_list, target_number))
    print('result - ', some_list)