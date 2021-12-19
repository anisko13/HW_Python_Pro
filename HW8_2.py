def result_function():
    fib = 1
    fib_prev = 1
    # 1, 1, 2, 3, 5, 8, 13
    
    def fib_count(n):
        step = 0    
        nonlocal fib
        nonlocal fib_prev
        while step < n:
            new_fib = fib_prev + fib_prev
            fib_prev = fib
            fib = new_fib
            step += 1
        return fib
    return fib_count

if __name__ == '__main__':
    result = result_function()
    print(result(6))