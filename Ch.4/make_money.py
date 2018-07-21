money_to_make = int(input("Type the money that you want to make! "))

user_money = [[10,000,0] , [5,000,0] , [1,000,0] , [500,0] ,
              [100,0], [50,0] , [10,0]]


for i in range(7):
    user_money[i][1] = int(input("How many %d-won do you have? : " % user_money[i][0]))

money_divide(user_money[i][0],money_to_make)

def money_divide(j,left_mon):
    minus_mon = user_money[j][0]* user_money[j][1]
    
    if minus_mon != 0:
        money_divide(j-1,left_mon)
    else:
        return 
