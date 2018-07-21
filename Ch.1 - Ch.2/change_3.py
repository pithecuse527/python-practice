x = int(input("x값을 입력하시오. "))
y = int(input("y값을 입력하시오. "))
z = int(input("z값을 입력하시오. "))

temp = x;
x = y;
y = z;
z = temp;

print("""x값 : %s
y값 : %s
z값 : %s""" % (x,y,z))
