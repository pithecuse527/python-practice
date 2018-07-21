##
#   18.03.08
#   20152262    Hong Geun Ji
#
#   Change the temperature to ctemp or ftemp

def change_to_C(ftemp):
    ctemp = (ftemp-32.0) * 5.0 / 9.0
    print(ctemp)

def change_to_F(ctemp):
    ftemp =(9.0 / 5.0) * ctemp + 32.0
    print(ftemp)

temp = float(input("온도를 입력하시오."))
change_to_F(temp)
