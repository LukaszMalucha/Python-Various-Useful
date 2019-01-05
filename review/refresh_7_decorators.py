# -*- coding: utf-8 -*-



##################################################################### Decorators

def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(fn.__name__, count)
        return fn(*args, **kwargs) 
    
    return inner

def add(a: int, b:int = 0):
    return a + b


add = counter(add)


def timed(fn, reps):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args,**kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / reps
        print(avg_elapsed)
        return result
    return inner

@timed
def my_func():
    pass