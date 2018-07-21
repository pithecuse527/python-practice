def selectionSort_min(alist):
    for i in range(len(alist)):
        minPos = getMinPos(alist,i)
        
        temp = alist[minPos]
        alist[minPos] = alist[i]
        alist[i] = temp

def getMinPos(alist, start):
    minPos = start
    for i in range(start+1, len(alist)):
        if alist[i] < alist[minPos]:
            minPos = i
    return minPos

def selectionSort_max(alist):
    for i in range(len(alist)):
        maxPos = getMaxPos(alist,i)
        temp = alist[maxPos]
        alist[maxPos] = alist[i]
        alist[i] = temp

def getMaxPos(alist, start):
    maxPos = start
    for i in range(start+1, len(alist)):
        if alist[i] > alist[maxPos]:
            maxPos = i
    return maxPos


lis = [1,2,3,4,5,6,7]
lis2 = [7,6,5,4,3,2,1]
selectionSort_max(lis)
selectionSort_min(lis2)

print(lis)
print(lis2)
