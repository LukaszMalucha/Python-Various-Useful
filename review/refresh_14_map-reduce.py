# -*- coding: utf-8 -*-


maps = map(lambda x: x**2, range(5))

type(maps)


list(maps)

def add(t):
    return t[0] + t[1]

list(map(add, [(0,0), [1,1], range(2,4)]))


######################################################################## StarMap

from itertools import starmap

def add(x,y):
    return x + y

list(starmap(add, [(0,0), (1,1), (2,3)]))