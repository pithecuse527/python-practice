STUDENT = 10

def switch(lis, i, j) :
    tmp = lis[i]
    lis[i] = lis[j]
    lis[j] = tmp
    return lis[i]
    

scores = []
scoreSum = 0

for i in range(STUDENT) :
    value = int(input("성적을 입력하시오 "))
    scores.append(value)
    scoreSum += value

scoreAvg = scoreSum / len(scores)

#scoreMax = max(scores)
#scoreMin = min(scores)


#selectionSort
for i in range(0,STUDENT) :
    min = scores[i]
    for j in range(i+1,STUDENT) :
        if scores[j] < min :
            #tmp = scores[i]
            #scores[i] = scores[j]
            #scores[j] = tmp
            #min = scores[i]
            min = switch(scores, i, j)

print("성적 평균은", scoreAvg, "입니다.")
print("성적 최저는", scores[0], "입니다.")
print("성적 최고는", scores[9], "입니다.")
    
