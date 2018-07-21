p1x = int(input("p1x "))
p1y = int(input("p1y "))

p2x = int(input("p2x "))
p2y = int(input("p2y "))

p3x = int(input("p3x "))
p3y = int(input("p3y "))

p4x = int(input("p4x "))
p4y = int(input("p4y "))

overlapped = not ( ( p2y > p3y and p2y > p4y ) or ( p1y < p4y and p1y < p3y ) or
                   ( p2x < p3x and p2x < p4x ) or ( p1x > p4x and p1x > p3x ) )

if overlapped :
    print("겹침!")

else :
    print("안겹침!")
