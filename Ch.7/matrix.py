#
#
#   18.05.03
#   리스트에 관한 문제 : 2개의 행렬 합 계산하기
#

s1 = []
s2 = []

m1 = int(input("첫 번째 행렬의 행 : "))
n1 = int(input("첫 번째 행렬의 열 : "))

for i in range(n1+1) :          # 행렬 초기화
    s1 += [[0]*n1]

for i in range(m1) :            # 행렬의 값 입력하는 부분
    for j in range(n1) :
        s1[i][j] = int(input("%d행 %d열 값 : " % (i+1,j+1)))
        
print("\n\n")

for i in range(m1) :            # 행렬의 값 출력하는 부분
    for j in range(n1) :
        print(" %d " % s1[i][j], end="    ")
    print("\n")



m2 = int(input("두 번째 행렬의 행 : "))
n2 = int(input("두 번째 행렬의 열 : "))

for m2 in range(n2+1) :         # 행렬 초기화 
    s2 += [[0]*n2]

for i in range(m2) :            # 행렬의 값 입력하는 부분
    for j in range(n2) :
       s2[i][j] = int(input("%d행 %d열 값 : " % (i+1,j+1)))
       
print("\n")

for i in range(m2) :            # 행렬의 값 출력하는 부분
    for j in range(n2) :
        print(" %d " % s2[i][j], end="    ")
    print("\n")

print("\n==========결과==========\n")


if m1 == m2 and n1 == n2 :          # 행과 열이 서로 일치해야 계산.
    for i in range(m1) :
        for j in range(n1) :
            s1[i][j] += s2[i][j]
            print(" %d " % s1[i][j], end="    ")
        print("\n")
    
else :
    print("행과 열이 서로 맞지 않습니다.")
