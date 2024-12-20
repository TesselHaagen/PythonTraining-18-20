import math 
from functools import total_ordering

@total_ordering
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    
    def __eq__(self, other):
        return len(self) == len(other)
    
    def __gt__(self, other):
        return len(self) > len(other)
    
vector1 = Vector(5,6)
vector2 = Vector(2,3)

vector3 = vector1 + vector2
print(vector3)
print(vector1 > vector2)
print(vector1 >= vector2)