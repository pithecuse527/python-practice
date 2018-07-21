#
#
#   18.05.17
#   로또 번호 발생기 + 중복되는 값까지 고려.
#



import random

myList = set()

while True:
    n = random.randint(1,45)
    if n not in myList:         # 중복이 안된다면 add.
        myList.add(n)
    if len(myList) == 6:
        break

# 다른 방법. 
'''
while True:
    n = random.randint(1,45)
    if n in myList:
        continue
    else:
        myList.add(n)
    if len(myList) == 6:
        break
'''

print(sorted(myList))
#print(myList.sorted())       # 파이썬 버전3 부터는 사용 불가. (집합, 튜플, 딕셔너리 또한) 
