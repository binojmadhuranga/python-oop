"""Simple Abstraction Example

Abstraction = Hiding complex details, showing only essential features
Using ABC (Abstract Base Class) to define a blueprint
"""

from abc import ABC, abstractmethod

# Abstract class - cannot create objects from it
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


# Concrete class 1
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


# Concrete class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius


# Demo
if __name__ == "__main__":
    # Cannot create: shape = Shape()  # Error!
    
    rect = Rectangle(5, 3)
    circle = Circle(4)
    
    print(f"Rectangle area: {rect.area()}")
    print(f"Rectangle perimeter: {rect.perimeter()}")
    
    print(f"\nCircle area: {circle.area()}")
    print(f"Circle perimeter: {circle.perimeter()}")
