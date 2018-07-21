from math import *

x1 = int(input("Type the x1 : "))
y1 = int(input("Type the y1 : "))
x2 = int(input("Type the x2 : "))
y2 = int(input("Type the y2 : "))

distance = sqrt((y2**2 - y1**2) / (x2**2 - x1**2))

print(distance)
