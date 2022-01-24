from time import time

def timer(func):
    def wrap_func(*args, **kwargs):
        time1 = time()
        result = func(*args, **kwargs)
        time2 = time()
        print(f'Function {func.__name__!r} executed in {(time2 - time1):} sec')
        return result
    return wrap_func

@timer
def calcTime(n):
    for i in range(n):
        for j in range(n * n):
            i + j - i + j
            if n>0:
                i-1;

calcTime(60)
