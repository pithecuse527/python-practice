def sel_sort(aList,reverse=False):
    
    for i in range(len(aList)-1):
        max_val = aList[i]
        for j in range(i+1, len(aList)):
            if compare(max_val, aList[j], reverse):
                max_val = aList[j]
                aList[i], aList[j] = aList[j], aList[i]

def compare(least_val, aList, reverse):
    if not reverse:
        return (least_val > aList)
    return (least_val < aList)


list1 = []
tmp = 0
while True:
    print("입력을 중단하려면 -1을 입력하시오.\n")
    tmp = int(input("숫자를 입력하시오."))
    if tmp == -1:
        break
    list1.append(tmp)
            
sel_sort(list1,reverse=True)
print(list1)
            
