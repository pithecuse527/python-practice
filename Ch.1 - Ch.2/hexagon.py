##
#   18.03.08
#   20152262    Hong Geun Ji
#
#   Using turtle to draw hexagon.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

i = 1

while i < 7:
    t.forward(150)
    t.right(60)
    print(i)
    i += 1

for j in range(6):
    t.forward(150)
    t.right(60)

