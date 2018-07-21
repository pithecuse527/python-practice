theta = [0,0,0]

i = 0
sum = 0

while i < 3 :
        theta[i] = float(input("Type the %s angle of triangle " % str(i+1)))
        sum += theta[i]
        if theta[i] == 0:
                is_zero = True
        i += 1

if sum != 180 or not(is_zero):
    print("Wrong input!")
else :
    if (theta[0] < 90) and (theta[1] < 90) and (theta[2] < 90):
        print("예각입니다.")
    elif (theta[0] == 90) or (theta[1] == 90) or (theta[2] == 90):
        print("직각입니다.")
    else:
        print("둔각입니다.")
        
