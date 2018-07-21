PI = 3.14

class Shape:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getType(self):
        return self.__class__.__name__
    def getName(self):
        for key, val in globals().items():
            if val is self:
                return key
    def noArea(self):           
        print("계산할 수 없음!")
    def noPerimeter(self):
        print("계산할 수 없음!")
    def __str__(self):
        return "Area of " + self.getName() + " : " + str(self.getArea()) + "\n" +\
               "Perimeter of " +self.getName() + " : " + str(self.getPerimeter())

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.__r = r
    def getArea(self):
        if not self.__r:
            self.noArea()
            return
        return (self.__r)**2 * PI       # PI is Constant
    def getPerimeter(self):
        if not self.__r:
            self.noPerimeter(self)
            return
        return 2 * PI * r
    def __str__(self):
        return "Area of " + self.getName() + " : " + str(self.getArea()) + "\n" +\
               "Perimeter of " +self.getName() + " : " + str(self.getPerimeter())


class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.__w = w
        self.__h = h
    def getArea(self):
        if not (self.__w and self.__h):
            self.noArea()
            return
        return self.__w * self.__h
    def getPerimeter(self):
        if not (self.__w and self.__h):
            self.noPerimeter()
            return
        return 2 * (self.__w + self.__h)
    def __str__(self):
        return "Area of " + self.getName() + " : " + str(self.getArea()) + "\n" +\
               "Perimeter of " +self.getName() + " : " + str(self.getPerimeter())


class Square(Rectangle):            # 정사각형 클래스
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)   # 여기서 r을 모두 전달하면 됨
        self.__r = r
    def __str__(self):
        return "Type : " + self.getType() + "\n" +\
               "Area of " + self.getName() + " : " + str(self.getArea()) + "\n" +\
               "Perimeter of " +self.getName() + " : " + str(self.getPerimeter())

squ1 = Square(1,2,9)
rec1 = Rectangle(2,3,5,7)

#print("정사각형의 면적", squ1.getArea())
#print("정사각형의 둘레", squ1.getPerimeter())
#print(squ1)
print(squ1)
