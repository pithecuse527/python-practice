x = float(input("x의 좌표를 입력하세요. "))
y = float(input("y의 좌표를 입력하세요. "))

if x > 0 and y > 0 :
    print("1사분면")
elif x < 0 and y > 0 :
    print("2사분면")
elif x < 0 and y < 0 :
    print("3사분면")
elif x > 0 and y < 0 :
    print("4사분면")
