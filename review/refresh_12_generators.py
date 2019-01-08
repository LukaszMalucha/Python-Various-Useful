# -*- coding: utf-8 -*-

import math

########################################################################## Yield


## non-yield

def fact():
    i = 0
    def inner():
        nonlocal i 
        result = math.factorial(i)
        i = i + 1
        return result
    return inner

f = fact()

f()


fact_iter = iter(fact(), math.factorial(5))

list(fact_iter)


########### Yield - Generator Factory

def my_func():
    yield 'Flying'
    yield 'Circus'
    yield 'of'
    return 'Done'
    yield 'Monty'
   
    
y = my_func()

result = next(y)

result    


for line in y:
    print(line)
    
    
def fact(n):
    for i in range(n):
        yield math.factorial(i)    
    
gen = fact(5)

next(gen)    
    
    
###################################################################### Fibonacci    
    
################## slow    

from functools import lru_cache

#lru_cache()
def fib_recursive(n):
    if n <=1: 
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
    
[fib_recursive(i) for i in range(7)]
    
    
#################### fast

def fib(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1   
    yield fib_1
    for i in range(n-2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1    
    
f = fib(10)    
    
for num in f:
    print(num)
    
    
######################################################## Iterable from Generator      




class Squares: 
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return Squares.squares_gen(self.n)
    
    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield i ** 2
    
sq = Squares(5)     
    
    
for num in sq:
    print(num)    
    
list(sq)        
    
    
### enumerator

def squares(n):
    for i in range(n):
        yield i ** 2   
    
sq = squares(5)

enum_sq = enumerate(sq)
list(enum_sq)

















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    