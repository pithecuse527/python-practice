import random, time
myList = ["head", "tail"]

start_t = time.time()
while True:
    response = input("동전 던지기를 계속? (Y/N) ")
    if response == 'Y':
        coin = random.choice(myList)
        print(coin)
    elif response == 'N':
        break
    else:
        print("잘못된 입력!")
finish_t = time.time()
print(finish_t - start_t)
