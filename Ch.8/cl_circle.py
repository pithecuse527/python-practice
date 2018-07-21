import math

class Circle:
    def __init__(self, radius=1.0):
        self._-radius = radius

    def setRadius(self, r):
        self.__radius = r

    def getRadius(self):
        return self.__radius

    def calcArea(self):
        area = (math.pi) * (self.__radius ** 2)

    def calcCircum(self):
        circumference = 2 * math.pi * self.__radius
        return circumference

c1 = Circle(10)

print("원의 반지름 = ", c1.getRadius())
print("원의 넓이 = ", c1.clcArea())
print("원의 둘레 = ", c1.calcCircum())
