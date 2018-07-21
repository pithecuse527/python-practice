#
##
#   UOU Python Programming
#   2018.06.07  HONGGEUN JI     20152262
#   Title : Recursion selection sort.
##
#

def selectionSort(alist, from_ = 0, mode = "Ascending"):
    if from_ == len(alist) - 1:     # returning condition
        return
    
    thePos = from_          # Where to start

    for i in range(from_ + 1, len(alist)):      # compare and changing process
        if checkByMode(alist, i, thePos, mode):
            tmp = alist[i]
            alist[i] = alist[thePos]
            alist[thePos] = tmp

    selectionSort(alist, from_+1, mode)         # Recurssion process


def checkByMode(alist, i, thePos, mode):
    if mode == "Ascending":
        return alist[i] < alist[thePos]
    else:
        return alist[i] > alist[thePos]

def main():
    lis2 = [5,1,6,2,3,9,10]
    selectionSort(lis2, mode = "Descending")
    print(lis2)

main()          
