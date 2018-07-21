x = int(input("첫 번째 정수: "))
y = int(input("두 번째 정수: "))
z = int(input("세 번째 정수: "))


if (x > y) :
    max = x
else :
    max = y

if z > max :
    max = z       

print(max)
