sentence = input("문자열을 입력하시오: ")

table = {"Upper-alphas" : 0, "Lower-alphas" : 0, "digits" : 0, "spaces" : 0}

for i in sentence :
    if i.isupper() :
        table["Upper-alphas"] += 1
    elif i.islower() :
        table["Lower-alphas"] += 1
    elif i.isdigit() :
        table["digits"] += 1
    elif i.isspace() :
        table["spaces"] += 1

print(table)
