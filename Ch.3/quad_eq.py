import math

a = float(input("2차항 계수를 입력하시오. "))
b = float(input("1차항 계수를 입력하시오. "))
c = float(input("상수항 계수를 입력하시오. "))

D = b*b - 4*a*c

if a == 0 :
    x = -c/b
else :
    if D > 0 :
        x = (-b + math.sqrt(D)) / (2 * a)
        print("근은",x,end=" ")
        x = (-b - math.sqrt(D)) / (2 * a)
        print(x)
        
    elif D == 0 :
        x = -b / 2*a
        print("근은",x)
    else :
        print("근이 없습니다.")
    
    
