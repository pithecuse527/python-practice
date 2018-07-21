x = [0,0,0]

i = 0
while i < 3 :
    x[i] = int(input("%s번째 숫자를 입력하시오." % str(i+1)) )
    i += 1
    
max = 0

if x[0] < x[1] :
    max = x[1]
else :
    max = x[0]

if max < x[2] :
    max = x[2]

print("가장 큰 수는 :",max)

    
