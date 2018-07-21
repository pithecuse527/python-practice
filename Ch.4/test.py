n = int(input("어떤 구구단을 출력할까요? "))


print("\nfor로 출력\n")
for i in range(1,10) :
    
    print("%d * %d = %d" % (n,i,n*i))

print("\n===============\n")

print("while로 출력\n")
i = 1
while i < 10 :

    print("%d * %d = %d" % (n,i,n*i))
    i = i + 1
    
