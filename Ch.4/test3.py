gugu_st = int(input("시작할 구구단 : "))
gugu_en = int(input("끝나는 구구단 : "))

for i in range(gugu_st,gugu_en + 1) :
    print("\n==========%d단==========\n" % i)
    for j in range(1, 20) :
        print("%d * %d = %d" % (i, j, i*j))
    print("\n====================\n")

