#
#
#   18.05.03
#   회문 검사 (교재와 상이한 함수)
#


def is_cir(inpt):

    tmp = []
    inpt = inpt.lower()     # 모두 소문자로
    
    for x in list(inpt):     # inpt를 리스트로 만들어서 비교.
        if x.isalpha():      # x가 알파벳이면 tmp에 append.
            tmp.append(x)

    n = len(tmp)
    
    for i in range(n):
        if tmp[i] != tmp[n-(i+1)]:      # 회문 검사.
            return False
    return True

inpt = input("문자열을 입력하시오. ")
if is_cir(inpt):
    print("회문입니다.")
else :
    print("회문이 아닙니다.")
            
