from math import sqrt

class Point2D:
    x = 100
    y = 20

class Line2D:
    point1 = Point2D()
    point2 = Point2D()

    def distance(self):
        return sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)

a = Point2D
print(a.x)
print(a.y)

l = Line2D()
print(l.distance())
