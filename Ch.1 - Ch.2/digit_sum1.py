##
#
#   18.03.15       20152262    Hong Geun Ji
#   
#   Sum each number of digits.
#


num = int(input("Type four-digit natural number : "))

while (num // 1000 > 9) or (num // 1000 == 0) :
    print("Your value is not a four-digit natural number!")
    num = int(input("Type four-digit natural number : "))

n = 3
digit_sum = 0

while n >= 0:
    digit_sum += num // 10**n   # digit_sum = digit_sum + (num // 10**n)
    num %= 10**n                # num = num % 10**n
    n -= 1                      # n = n - 1

print(digit_sum)
