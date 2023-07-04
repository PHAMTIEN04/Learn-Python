# Question 1: Write classes Shape (abstract) and Circle, Square, Rectangle,
# Ellipse, Sphere. Design your inheritance properly.
# Abstract Method
from abc import ABC, abstractmethod
from math import sqrt
class Shape:
    PI = 3.14
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def acreage(self):
        pass
    @abstractmethod
    def volume(self):
        pass



class Circle(Shape):
    
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        pe = 2*Shape.PI*self.r
        round_pe = round(pe,1)
        return round_pe
    def acreage(self):
        ac = Shape.PI * (self.r ** 2)
        round_ac = round(ac,1)
        return round_ac

class Square(Shape):
    def __init__(self,s):
        self.s = s
    def perimeter(self):
        pe = 4 * self.s
        round_pe = round(pe,1)
        return round_pe
    def acreage(self):
        ac = self.s ** 2
        round_ac = round(ac,1)
        return round_ac
class Rectangle(Shape):
    def __init__(self,a,b):
        self.a = a 
        self.b = b
    def perimeter(self):
        pe = 2*(self.a + self.b)
        round_pe = round(pe,1)
        return round_pe
    def acreage(self):
        ac = self.a * self.b 
        round_ac = round(ac,1)
        return round_ac

class Ellipse(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def perimeter(self):
        pe = (2*Shape.PI) * sqrt(((self.a ** 2) + (self.b ** 2))/2)
        round_pe = round(pe,1)
        return round_pe
    def acreage(self):
        ac = Shape.PI * self.a * self.b
        round_ac = round(ac,1)
        return round_ac

class Sphere(Shape):
    def __init__(self,r):
        self.r = r
    def acreage(self):
        ac = (4*Shape.PI)*(self.r ** 2)
        round_ac = round(ac,1)
        return round_ac
    def volume(self):
        vo = ((4/3)*Shape.PI) * (self.r ** 3)
        round_vo = round(vo,1)
        return round_vo
c = Circle(10)
print("**Circle**")
print("Perimeter :",c.perimeter())
print("Acreage :",c.acreage())

sq = Square(10)
print("**Square**")
print("Perimeter :",sq.perimeter())
print("Acreage :",sq.acreage())

re= Rectangle(10,20)
print("**Rectangle**")
print("Perimeter :",re.perimeter())
print("Acreage :",re.acreage())

el= Ellipse(10,20)
print("**Ellipse**")
print("Perimeter :",el.perimeter())
print("Acreage :",el.acreage())

s1= Sphere(10)
print("**Sphere**")
print("Perimeter :",s1.acreage())
print("Volume :",s1.volume())
    
    
