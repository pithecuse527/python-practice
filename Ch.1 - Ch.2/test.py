atnd_num = int(input("Type the number of attendence: "))

chicken = "chicken is " + str(atnd_num)
beer = "beer is " + str(atnd_num * 2)
cake = "cake is " + str(atnd_num * 4)

tmp = [chicken, beer, cake]

for i in tmp:
    print("The number of",i)
