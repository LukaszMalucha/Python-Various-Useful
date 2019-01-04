# -*- coding: utf-8 -*-


######################################################################### Lambda

lambda x,y: x + y
lambda s: s[::-1].upper()

my_func = lambda x: x**2

def apply_func(x, fn):
    return fn(x)
    
apply_func(3, my_func)    

def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)


######################################################################### Sorted

l = [1,5,4,10,9]

sorted(l)

l = ['c', 'B', 'D', 'a']
sorted(l, key=lambda s: s.upper())

d = {'defd': 300, 'abcz':200, 'ghia': 100}

sorted(d, key=lambda e: d[e])


sorted(d, key = lambda x: x[-1])

###Challenge:  Shuffle list with sorted and random.random
import random


l = [1,2,3,4,5,6,7,8,9,10]


sorted(l, key = lambda x: random.random())


################################################################## Introspection

dir(my_func)


###################################################################### Callables

callable(print)


################################################################ Map, Filter,Zip


def fact(n):
    return 1 if n < 2 else n * fact(n-1)

results = list (map(fact, range(6)))



l1= [1,2,3,4,5]
l2 = [10,20,30]

results = list(map(lambda x,y: x+y, l1,l2))
results = list(zip(l1,l2))

x = range(25)


for i in x:
    print(i)
    
results = list(filter(lambda x: x%3 == 0, range(25)))

results = list(zip(l1, l2))


############################################################# Reducing Functions

l = [5,8,6,10,9]
max_value = lambda a,b: a if a > b else b

def max_sequence(sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = max_value(result,e)
    return result    
        

from functools import reduce

l = [5,8,6,10,9]

reduce(lambda a,b: a if a > b else b, l)

reduce(lambda a,b: a if a > b else b, 'python')

reduce(lambda a, b: a + ' ' + b, ('python', 'is', 'awesome'))


############################################################## Partial Functions

f = lambda b, c: my_func(10,b,c)

from functools import partial

f = partial(my_func, 10)


################################################################ Operator Module

from operator import itemgetter

l = [1,2,3,4,5,6]
f = itemgetter(1,3,4) ## indices

f(l)



















