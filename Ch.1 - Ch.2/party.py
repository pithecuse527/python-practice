number = int(input("참석자의 수를 입력하시오: "))

chickens = ("치킨의 수: " + str(number))
beers = ("맥주의 수: " + str(number * 2))
cakes = ("케익의 수: " + str(number * 4))

tmp = [chickens,beers,cakes]

for i in tmp:
    print(i)
