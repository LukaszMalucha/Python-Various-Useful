# -*- coding: utf-8 -*-


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
### Access width through rectangle.width instead of width() through decorator         
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive.")
        else:
            self_width = width


    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("height must be positive.")
        else:
            self_height = height
    
       
    @property
    def height(self):
        return self._height
        
    def area(self):
        return self.width * self,height
    
    def perimiter(self):
        return 2 * (self.width + self.height)

    
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