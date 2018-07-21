num = int(input("금액을 입력하시오 :"))

count_of_10000 = 0
count_of_5000 = 0
count_of_1000 = 0

for i in range(0,(num//10000)+1) :
    count_of_10000 = i
    rest = num - (10000 * i)
    
    for j in range(0,(rest//5000)+1) :
        count_of_5000 = j
        
        rest2 = rest - (5000*j)
        
        count_of_1000 = rest2 // 1000
        
        print("천원 : %d개" % count_of_1000)
        print("오천원 : %d개" % count_of_5000)
        print("만원 : %d개" % count_of_10000)
        print("\n==========\n")
