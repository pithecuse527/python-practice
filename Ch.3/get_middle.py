usr_str = input("Input the sentence : ")

mid_num = len(usr_str) // 2

if len(usr_str) % 2 != 0 :
    print(usr_str[mid_num])
else :
    print(usr_str[mid_num], usr_str[mid_num+1])
