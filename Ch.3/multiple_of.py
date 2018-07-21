MAX_RATE = int(input("최댓값을 입력하세요. "))
num = int(input("무엇의 배수를 출력할까요? "))

i = 1
while i <= MAX_RATE :
    print("%s * %s = %s" % (num, i, num*i))
    i += 1
    
