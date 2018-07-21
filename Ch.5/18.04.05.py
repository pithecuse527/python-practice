from math import *

def triArea(b, h) :
    return 0.5 * b * h

def volCone(r, h) :
    vol = (1/3) * h * pi * r**2
    return round(vol, 5)

def divisor(n) :
    for i in range(1, n+1) :
        if n % i == 0 :
            print(i)

def is_prime(i) :
    for j in range(2, i) :
        if i % j == 0 :
            return False
    return True

def leap_year(year) :
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
        return True

def slope_intercept(x1, y1, x2, y2) :
    slope = float(y2 - y1) / float(x2 - x1)     # 기울기
    intercept_x = x2 - float(y2 / slope)        # x절편
    intercept_y = y2 - float(slope * x2)        # y절편

    return slope, intercept_x, intercept_y

def vol_area_Cone(r, h, l) :
    vol = (1/3) * h * pi * r**2
    area = (pi * r**2) + (pi * r * l)
    return vol, area

def common(a,b) :
    num = max(a,b)
    num2 = min(a,b)
    common_divisor = "없음"
    for i in range(2, num+1) :
        if a % i == 0 and b % i == 0 :
            common_divisor = i

    if common_divisor != "없음":
        common_multiple = (a*b) / common_divisor
    else :
        common_multiple = (a*b)
            
    print("최소공배수 : %s" % common_multiple)
    print("최대공약수 : %s" % common_divisor)
        

def main() :
    
    while True :
        print("\n")
        print("These are the functions you can choose. Type -1 to exit.")
        print("triArea, volCone, divisor, is_prime, leap_year, slope_intercept, vol_area_Cone, common")
        func = input("Type the function that you want : ")

        if func == "triArea" :
            b = float(input("밑변을 입력하시오. "))
            h = float(input("높이를 입력하시오. "))
            print("삼각형의 넓이는 : %s" % triArea(b,h))
            
        elif func == "volCone" :
            r = float(input("반지름을 입력하시오. "))
            h = float(input("높이를 입력하시오. "))
            print("원뿔의 부피는 : %s " % volCone(r,h))
            
        elif func == "divisor" :
            n = int(input("어떤 자연수의 약수를 출력할까요? "))
            divisor(n)
            
        elif func == "is_prime" :
            m = int(input("시작 자연수 : "))
            n = int(input("마지막 자연수 : "))
            print("m부터 n까지의 소수는 다음과 같습니다.")
            for i in range(m, n+1) :
                if is_prime(i) :
                    print(i)
                    
        elif func == "leap_year" :
            start = int(input("시작 연도를 입력하시오. "))
            finish = int(input("어느 연도까지 윤년을 구할까요? "))
            for i in range(start, finish+1):
                if leap_year(i) :
                    print(i)
                    
        elif func == "slope_intercept" :
            x1 = int(input("x1을 입력하시오. "))
            y1 = int(input("y1을 입력하시오. "))
            x2 = int(input("x2을 입력하시오. "))
            y2 = int(input("y2을 입력하시오. "))
            slope, intercept_x, intercept_y = slope_intercept(x1,y1,x2,y2)
            print("기울기 = %s   x절편 = %s    y절편 = %s" % (slope, intercept_x, intercept_y))
            
        elif func == "vol_area_Cone" :
            r = float(input("반지름을 입력하시오. "))
            h = float(input("높이를 입력하시오. "))
            l = float(input("모선을 입력하시오. "))
            vol, area = vol_area_Cone(r, h, l)
            print("원뿔의 부피는 : %f" % vol)
            print("원뿔의 넓이는 : %f" % area)

        elif func == "common" :
            a = int(input("첫번째 숫자를 입력하시오. "))
            b = int(input("두번째 숫자를 입력하시오. "))
            common(a,b)
            
        elif func == "-1":
            break
        
        else :
            print("Invalid type! Please check your input.")

main()
        
        


            
            
            
        
        
