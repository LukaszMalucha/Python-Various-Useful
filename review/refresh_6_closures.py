# -*- coding: utf-8 -*-


########################################################## Classes as a Closures

class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0
        
    def add(self, number):
        self.total = self.total + number
        self.count = self.count + 1     
        return self.total / self.count

a = Averager()

a.add(10)
a.add(20)

## Closure

def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1    
        return total / count     
    return add


from time import perf_counter

class Timer:
    def __init__(self):
        self.start = perf.counter()
        
    def __call__(self):
        return perf_counter() - self.start
    
    
    
def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    