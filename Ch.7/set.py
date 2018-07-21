setA = {x for x in range(101) if x % 3 == 0}
setB = {x for x in range(101) if x % 5 == 0}

setI = setA.intersection(setB)
setU = setA.union(setB)

print(setI)
print(setU)
