#
#
#   18.05.03
#   단어장 만들기 + 입력한 값이 올바른 값인지 검사하는 함수
#


input_eng = ""
input_kor = ""
inpt = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
dic = {"end" : ""}

def alpha_chk(inpt) :
    for x in inpt:              # 철자 하나하나씩 비교.
        if x not in alphabet:   # 만약 x가 알파벳이 아니면 False.
            return False
    return True

def han_chk(inpt):
    for x in inpt:
        if x in alphabet:       # 만약 x가 알파벳이면 False.
            return False
    return True

#while input_eng != "end" :
while True:
    print("==========입력을 끝내시려면 end를 입력하세요.==========")
    
    input_eng = input("영어 단어를 입력하세요 : ")
    if input_eng == "end" : break
    input_kor = input("한글 단어를 입력하세요 : ")
    if input_kor == "end" : break

    if not ( alpha_chk(input_eng) and han_chk(input_kor) ):
        print("\n 입력오류! 영어 단어는 영어만, 한글 단어는 한글만 입력!")
        continue            # 다시 입력하기

    dic[input_eng] = input_kor


while inpt != "end" :
    print("\n\n==========검색을 끝내시려면 end를 입력하세요.==========")
    inpt = input("찾을 단어를 입력하세요 : ")
    
    if alpha_chk(inpt) :        # 영어 단어만 입력.
        print(dic.get(inpt,"찾을 수 없는 단어"))
    else :
        print("영어만 입력하세요.")
    
