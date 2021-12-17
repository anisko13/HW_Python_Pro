def custom_generator(multiplier, limit):
    i = 1
    while i <= limit:
        i *= multiplier
        yield i
    return


if __name__ == '__main__':
    some_gen = custom_generator(5, 200)
    try:
        while True:
            if input() == 'stop':
                print('расчет окончен')
                break
            print(next(some_gen))
    except StopIteration:
        print('расчет окончен')
