##
#
#

r = float(input("반지름을 입력하시오 "))
h = float(input("높이를 입력하시오 "))
pi = 3.14

size = (r**2 * pi) * h
area = (2*pi*r) * h + (r**2 * pi) * 2

print("원기둥의 부피는", size)
print("원기둥의 겉넓이는", area)
