def readList() :
    nlist = []
    flag = True
    while flag :
        number = int(input("숫자를 입력하시오: "))
        if number < 0 :
            flag = False
        else :
            nlist.append(number)
    return nlist

def processList(nlist) :
    nlist.sort()

def printList(nlist) :
    for i in nlist :
        print("성적=", i)

# 점수를 합산해 돌려받는 함수를 추가한 후 실행
def listAdd(nlist) :
    tmp = 0
    for i in nlist :
        tmp += i
    return tmp

def main() :
    nlist = readList()
    processList(nlist)
    printList(nlist)
    sum = listAdd(nlist)
    print("성적의 합 : %d" % sum)

if __name__ == "__main__" :
    main()
else :
    main()
