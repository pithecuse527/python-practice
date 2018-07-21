
init_money = int(input("초기 자본을 입력하시오. "))
years = int(input("기간을 입력하시오. (연단위) "))
interest = float(input("이율을 입력하시오. "))

print("==========복리계산법==========")
c_interest = init_money * (1+interest)**years
print(init_money,years,interest,c_interest)

print("\n==========단리계산법==========")    
s_interest = init_money * (1+interest*years)
print(init_money,years,interest,s_interest)
