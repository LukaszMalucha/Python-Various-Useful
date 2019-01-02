# -*- coding: utf-8 -*-


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self,height
    
    def perimiter(self):
        return 2 * (self.width + self.height)
    
    
    def get_width(self):
        pass
    
    ## stringify
    def __str__(self):
        return ' {0} x {1} Rectangle'.format(self.width, self.height)
    
    ## representation
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    ## comparing ( for == )
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False
    
    ## implement less than    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented