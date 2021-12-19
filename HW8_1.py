def result_function(first, steps, func):
    current_step = 0
    value = first
    while current_step < steps:
        value = func(value)
        yield value
        current_step += 1

def sum_2_time(x):
    return x + x

if __name__ == '__main__':
    result = result_function(1, 10, sum_2_time)
    print(list(result))