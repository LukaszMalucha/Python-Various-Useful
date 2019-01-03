# -*- coding: utf-8 -*-




############################################################ Unpacking Iterables

a,b,c = [1,2,3]
a,b,c = 'XYZ'

a,b = b,a


######################################################################### * & **

l = [1,2,3,4,5,6]

## SAME:

a,b = l[0], l[1:]

a, *b = l

*a, b = l

a,b,c, *d = l

###

l1 = [1,2,3]

l2 = [4,5,6]

l = [*l1, *l2]

### **

d1 = {'p':1, 'y':2, 't':3, 'h':4 }
d2 = {'t':3, 'h':4}
d3 = {'h': 5, 'o': 6, 'n':7}

d = {**d1, **d2, **d3}


############################################################### Nested Unpacking

l = [1,2, [3,4]]

a,b, (c,d) = l

a, *b, (c, *d) = [1,2,3, 'python']


########################################################################## *args

def func1(a,b, *args):
    print(a)
    print(b)
    print(args)

    
####################################################################### **kwargs    
    
    
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    
func(1,2, x=100, y=200)    
      
    
########################################################################## Timer    

import time
from datetime import datetime

def time_it(fn, *args, rep=1, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)

time_it(print, 1,2,3, sep=' - ', end = ' ***\n', rep=5)



def log(msg, *,dt=None):
    dt = dt or datetime,utcnow()
    print('{0}: {1}'.format(dt,msg))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














