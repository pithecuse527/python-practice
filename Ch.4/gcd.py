x = int(input("정수를 입력(큰 수) : "))
y = int(input("정수를 입력(작은 수) : "))

while (y != 0):
    r = x % y
    x,y = y,r
print("최대 공약수는 %d입니다." % x)
