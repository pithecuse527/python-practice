n = int(input("어느 배수의 합을 구할까요? "))

sum = 0

for i in range(n,101,n):
    sum = sum + i

'''
i = n
while i < 101 :
    sum = sum + i
    i = i + n
'''

print("1부터 100사이의 모든 %d의 배수의 합은 %d입니다." % (n,sum))
