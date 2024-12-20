import math

class Shape():
    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        self.perimeter = 0 #self.calc_perimeter()
        self.surface = 0 #self.calc_surface()
    
    # def calc_perimeter(self):
    #     raise NotImplementedError
    
    # def calc_surface(self):
    #     raise NotImplementedError

    def __eq__(self, other):
        return self.surface == other.surface

    def __lt__(self, other):
        return self.surface < other.surface
    
    def __str__(self):
        return f'Shape with width of {self.width}'
    


class Circle(Shape):
    def __init__(self, *args):
        print(args)
        super().__init__(self, args)
        self.surface = self.calc_surface()
        self.perimeter = self.calc_perimeter()
    
    def calc_perimeter(self):
        return math.pi * self.width
    
    def calc_surface(self):
        return math.pi * ((self.width/2) ** 2)
    
    def __str__(self):
        return f'Circle with width of {self.width}'
    


class Square(Shape):
    def __init__(self, width):
        super().__init__(width)
        self.surface = self.calc_surface()
        self.perimeter = self.calc_perimeter()

    def calc_perimeter(self):
        return 4 * self.width
    
    def calc_surface(self):
        return self.width * self.width # self.width ** 2



circle = Circle(12, 13)
circle1 = Circle(15)
square = Square(10)

print(circle > square)
print(circle.surface - square.surface)

print(circle)
print(square)

print(circle < circle1)