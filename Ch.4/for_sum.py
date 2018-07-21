n = int(input("어디까지 계산? "))

sum = 0

for i in range (1,n+1) :
    sum = sum + i

print("1부터 %d까지의 합 : %d (for문으로 계산)" % (n,sum))


sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print("1부터 %d까지의 합 : %d (while문으로 계산)" % (n,sum))


k = int(input("어떤 배수의 합을 구할까요? "))
sum = 0

for j in range(k,n,k) :
    sum = sum + j

print("%d까지의 %d배수들의 합 : %d" % (n,k,sum))
