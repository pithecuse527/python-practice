from random import randint

win = 0
total = 0
user = 1

while user > 0:
    print("가위 : 1 // 바위 : 2 // 보 : 3")
    print("게임을 종료하시려면 0을 입력하세요.")

    user = int(input("입력하세요! "))
    computer = randint(1,3)

    if user > 0:
        if computer == 1 :
            if user == 1 :
                print("비김!")
            elif user == 2:
                print("이김!")
                win = win + 1
            else :
                print("짐!")
            total = total + 1
        elif computer == 2 :
            if user == 1 :
                print("짐!")
            elif user == 2:
                print("비김!")
            else :
                print("이김!")
                win = win + 1
            total = total + 1
        else :
            if user == 1 :
                print("이김!")
                win = win + 1
            elif user == 2:
                print("짐!")
            else :
                print("비김!")
            total = total + 1
        print("\n")
    else :
        print("승률 :" , (win/total * 100))
        
        
        

    
