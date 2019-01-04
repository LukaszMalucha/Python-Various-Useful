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




















