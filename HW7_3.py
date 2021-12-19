def prime_range(limit):
    index = 1
    while index < limit:
        index += 1
        try:
            for k in range(2, index):
                if index % k != 0:
                    continue
                raise ValueError
        except ValueError:
            continue
        yield index
    return


if __name__ == '__main__':
    print(list(prime_range(100)))