##
#
#   18.03.15       20152262    Hong Geun Ji
#   
#   Another version of "sum each number of digits."
#

chiper = int(input("Type the chiper that you want : "))
num = int(input("Type %d-digit natural number : " % chiper))


while (num // 10**(chiper - 1) > 9) or (num // 10**(chiper - 1) == 0) :
    print("Your value is not a %d-digit natural number!" % chiper)
    num = int(input("Type %d-digit natural number : " % chiper))

digit_sum = 0

while chiper > 0:
    
    #print(num // 10**(chiper - 1))
    
    digit_sum += num // 10**(chiper - 1)    # digit_sum = digit_sum + (num // 10**chiper - 1)
    num %= 10**(chiper - 1)                 # num = num % 10**(chiper - 1)
    chiper -= 1                             # chiper = chiper - 1

    #print("digit_sum : %s" % digit_sum)
    #print("num : %s" % num)
    #print("chiper : %s" % chiper)

print(digit_sum)
