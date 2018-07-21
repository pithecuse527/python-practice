p = [ [0,0] , [0,0] , [0,0] , [0,0] ]

i = 0

while i < 4 :
    p[i][0] = int(input("P%s의 x좌표 : " % str(i+1)))
    p[i][1] = int(input("P%s의 y좌표 : " % str(i+1)))
    i += 1


if not(p[1][1] > p[2][1] or p[0][1] < p[3][1] or
    p[1][0] < p[2][0] or p[0][0] > p[3][0]) :
    print("겹침!")
else :
    print("안겹침!")



'''
if (p[1][1] > p[2][1] and p[1][1] > p[3][1]):
    print("정상1")
elif (p[1][0] < p[2][0] and p[1][0] < p[3][0]):
    print("정상2")
elif (p[0][1] < p[3][1] and p[0][1] < p[3][1]):
    print("정상3")
elif (p[0][0] > p[2][0] and p[0][0] > p[3][0]):
    print("정상4")
else :
    print("비정상!")
'''

overlapped = not( p[3][0] < p[1][0] or p[2][0] > p[1][0] or
                  p[1][1] < p[2][1] or p[0][1] > p[3][1])

if overlapped :
    print("겹침")
else :
    print("안겹침")
