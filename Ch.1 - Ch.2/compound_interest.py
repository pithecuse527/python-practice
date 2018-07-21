init_money = [24,25,26]
years = [382,383,384]
interest = [0.06, 0.07, 0.08]

print("==========복리계산법==========")
for i in range(3):
    c_interest = init_money[i] * (1+interest[i])**years[i]
    print(init_money[i],years[i],interest[i],c_interest)

print("\n==========단리계산법==========")    
for i in range(3):
    s_interest = init_money[i] * (1+interest[i]*years[i])
    print(init_money[i],years[i],interest[i],s_interest)



