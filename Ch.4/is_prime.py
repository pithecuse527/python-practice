num = int(input("임의의 자연수를 입력하시오. "))

is_prime = True

if num > 0 :
    for i in range(2,num) :
        if num % i == 0 :
             is_prime = False            
else :
    print("자연수가 아닙니다.")

if is_prime :
    print("소수입니다.")
else :
    print("소수가 아닙니다.")

num = int(input("어디까지 소수를 출력할까요? "))


for i in range(4,num+1) :
    is_prime = True
    for j in range(2,i):
        if i % j == 0 :
            is_prime = False
    if is_prime :
        print(i)
        
    
