import math
class Shape:
    def __init__area(self):
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__Rectangle(self, length, width):
        self.lenght = length
        self.width = width
        
    def area(self):
        return self.length * self.width    
    
    
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2) 