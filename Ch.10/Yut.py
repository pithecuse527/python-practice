import random

list_Yut = ['도','개','걸','윷','모']

while True:
    response = input("윷 던지기를 계속? (Y/N) ")
    if response == 'Y':
        yut = random.choice(list_Yut)
        print(yut)
    elif response == 'N':
        break
    else:
        print("잘못된 입력!")
