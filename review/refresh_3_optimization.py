# -*- coding: utf-8 -*-

import sys

###################################################################### INTERNING


a = 10
b = 10

a is b


############################################################### STRING INTERNING

a = 'some_long_string'
b = 'some_long_string'

sys.intern('some_long_string')

a = "hello"

b = "hello"

print(id(a), id(b))


a = "hello world"
b = "hello world"

print(id(a), id(b))

a = "hello_world"
b = "hello_world"

print(id(a), id(b))


####################################################################### PEEPHOLE

def my_func():
    a = 24 * 60
    b = (1,2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3
    
## check for compiled costants    
my_func.__code__.co_consts    





















