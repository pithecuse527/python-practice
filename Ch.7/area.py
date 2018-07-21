def cal_area(x, y) :
    return x*y, 2*x+2*y

x = int(input("가로의 길이 : "))
y = int(input("세로의 길이 : "))

print("넓이 : %d, 둘레 : %d" % cal_area(x, y))
