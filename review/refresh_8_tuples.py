# -*- coding: utf-8 -*-


######################################################################### Tuples

new_york = ('New York', 'USA', '8.500.000')

city, country, population = new_york

city, _, population = ('Beijing', 'China', '21.000.000')

record = ('New York', 'USA', '8.500.000', 'Beijing', 'China', '21.000.000' )

city, example, asd, zzz, *_. close = record 


################################################################### Named Tuples

class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
        
from collections import namedtuple

Point2D = namedtuple('Point2D', ['x', 'y'])

pt1 = Point2D(10, 20)

        
        
        