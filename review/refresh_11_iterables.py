# -*- coding: utf-8 -*-




########################################################## Iterating Collections

class Squares:
    def __init__(self, length):
        self.i = 0
        self.length = length
    
    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:    
            result = self.i ** 2
            self.i += 1
            return result
##        
    def __iter__(self):
        return self
        
sq = Squares(5)    
    
#while True:
#    try:
#        item = next(sq)
#        print(item)
#    except StopIteration:
#        break

for item in sq:
    print(item)
    
    
############################################################ Iterator & Iterable 

class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'London']
        self._index = 0
        
    def __len__(self):    
        return len(self._cities)
        
class CityIterator:
    
    def __init__(self, cities):
        self._cities = cities
        self._index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._cities[self._index]
            self._index += 1
            return item
            
cities = Cities()

city_iterator = CityIterator(cities)

for city in city_iterator:
    print(city)


################################################################# Lazy Iterables

## lazy eval

class Actor:
    def __init__(self, actor_id):
        self.actor_id = actor_id
        self.bio  = get_bio_db(actor_id)
        self.movies = None
        
    @property
    def movies(self):
        if self.movies is None:
            self.movies = lookup_db(self.actor_id)
        return self.movies    


############################################################# Built-in Iterables

## iterable
range(10)


## iterators
zip(l1,l2)
enumerate(l1)
open('asd.csv')
dictionary.keys() /keys /values

## list
with open('cars.csv') as f:
    l = f.readlines()


############################################################## Sorting Iterables

import random

random.seed(0)

for _ in range(10):
    print(random.randint(1,10))
    
    
class RandomInts:
    def __init__(self, length, *, seed=0, lower=0, upper=10):
        self.length = length
        self.seed = seed
        self.lower = lower
        self.upper = upper
        
    def __length__(self):
        return self.length
    
    def __iter__(self):
        return self.RandomIterator(self.length, seed = self.seed, lower = self.lower, upper = self.upper)
        
        
        
    class RandomIterator:     
        def __init__(self, length, *, seed, lower, upper):
            self.length = length
            self.lower = lower
            self.upper = upper
            self.num_requests = 0
            random.seed(seed)
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.num_requests >= self.length:
                raise StopIteration
            else:
                result = random.randint(self.lower, self.upper)
        
            
randoms = RandomInts(10)        

for num in randoms:
    print(num)
        
        
############################################################## Iterate Callables 


def counter():
    i = 0
    
    def inc():
        nonlocal i
        i += 1
        return i
    
    return inc


class CounterIterator:
    def __init__(self, counter_callable, sentinel):
        self.counter_callable = counter_callable
        self.sentinel = sentinel
        
        
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.counter_callable()
        if result == self.sentinel:
            raise StopIteration
        else:
            return result
        
        

cnt = counter()

cnt_iter = CounterIterator(cnt)

for _ in range(5):
    print(next(cnt_iter))        
        
        
        
############################################################## Reverse Iteration         
        
## Copy sequence
for item in seq[::-1]:
    print(item)
        
        
for i in range(len(seq)):
    print(seq[len(seq)] - i - 1)        
    
for i in range(len(seq)-1, -1, -1):
    print(seq[i])    
        
        
for item in reversed(seq):
    print(item)        
        
###################################################################### Card Deck   

_SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs') 
_RANKS = tuple(range(2,11)) + tuple('JQKA')

from collections import namedtuple

Card = namedtuple('Card', 'rank suit')

class CardDeck:
    def __init__(self):
        self.length = len(_SUITS) * len(_RANKS)

    def __len__(self):
        return self.length
    
    def __iter__(self):
        return self.CardDeckIterator(self.length)
    
    def __reversed__(self):
        return self.CardDeckIterator(self.length, reverse=True)
    
    class CardDeckIterator:
        def __init__(self, length, reverse=False):
            self.length = length
            self.reverse = reverse
            self.i = 0
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - 1 - self.i
                else:
                    index = self.i
                suit = _SUITS[index // len(_RANKS)]
                rank = _RANKS[index % len(_RANKS)]
                self.i = 0
                return Card(rank, suit)
                
            

deck = reversed(CardDeck())

for card in deck:
    print(card)






















     
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    























































