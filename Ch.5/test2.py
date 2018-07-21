def factorial(n) :
    result = 1
    for i in range(n,0,-1):
        result = result * i
    return result


num = int(input("어떤수의 factorial을 구할까요? "))
print("결과는 %d" % factorial(num))
