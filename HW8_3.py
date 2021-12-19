def result_function(lst):
    
    def mapper_func(func):
        nonlocal lst
        for index, elem in enumerate(lst):
            lst[index] = func(elem)
        return sum(lst)
    
    return mapper_func

def func_multiplier(x):
    return x * x

if __name__ == '__main__':
    result = result_function([1, 2, 4])
    print(result(func_multiplier))