def linearSearch(aList, key) :
    for i in range(len(aList)):
        if key == aList[i]:
            return i
    return 0

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

position = linearSearch(numbers, 80)

if position:
    print("탐색 성공 위치 =", position)
else:
    print("탐색 실패")
