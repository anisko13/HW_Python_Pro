import time

def chronic(times, filename):
    def wrapper(f):
        def wrapper2(*args):
            step = 0
            time_start = time.time()
            while step < times:
                print(step, times)
                step += 1
                f(*args)
            with open(filename+'.txt', 'w') as file:
                file.write(str(time.time() - time_start))
        return wrapper2
    return wrapper

@chronic(3, 'chronic')
def print_bye():
    time.sleep(2)
    print('bye')
print_bye()