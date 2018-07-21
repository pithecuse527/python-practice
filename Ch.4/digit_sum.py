num = int(input("임의의 수를 입력하시오. "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
