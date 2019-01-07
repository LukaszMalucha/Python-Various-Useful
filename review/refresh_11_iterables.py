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

with open('cars.csv') as f:
    l = f.readlines()




























































