x1 = float(input("x1의 좌표를 입력하세요. "))
y1 = float(input("y1의 좌표를 입력하세요. "))

x2 = float(input("x2의 좌표를 입력하세요. "))
y2 = float(input("y2의 좌표를 입력하세요. "))


if x1 == x2 and x1 < 0 :        # 기울기가 0인 경우들
    print("2,3 사분면을 지남")
elif x1 == x2 and x1 > 0 :
    print("1,4 사분면을 지남")
elif y1 == y2 and y1 < 0 :
    print("3,4 사분면을 지남")
elif y1 == y2 and y1 > 0 :
    print("1,2 사분면을 지남")
    
else:                           
    slope = (y2 - y1) / (x2 - x1)
    y_intercepting = -(slope * x1) + y1
    
    if slope > 0 :
        if y_intercepting < 0 :
            print("1,3,4사분면을 지남")
        elif y_intercepting == 0 :
            print("1,3사분면을 지남")
        else :
            print("1,2,3사분면을 지남")
    else :
        if y_intercepting > 0 :
            print("1,2,4사분면을 지남")
        elif y_intercepting == 0 :
            print("2,3사분면을 지남")
        else :
            print("2,3,4사분면을 지남")
    


    
