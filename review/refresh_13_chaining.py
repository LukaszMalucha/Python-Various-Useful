# -*- coding: utf-8 -*-


####################################################################### Chaining

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))

for gen in l1, l2, l3:
    for item in gen:
        print(item)
        
        
def chain_iterables(*iterables):
    for iterable in iterables:
        yield from iterable        
        
for item in chain_iterable(l1,l2,l3):
    print(item)        
    
    
from itertools import chain

for item in chain(l1,l2,l3):
    print(item)     
    
lists = [l1,l2,l3]

for item in chain(*lists):
    print(item)
    