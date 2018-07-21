class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
 
    def setting(self, width = __width, height = __height):
        self.__width = width
        self.__height = height
        print("너비 : %3f \n높이 : %3f" % (self.__width, self.__height))
    
    def set_width(self, width):
        if width <= 0:
            print("0보다 큰 값만 입력하시오.")
        else:
            self.__width = width
            print("너비 : %3f" % self.__width)

    def get_width(self):
        return self.__width

    def set_height(self, height):
        if height <= 0:
            print("0보다 큰 값만 입력하시오.")
        else:
            self.__height = height
            print("높이 : %3f" % self.__height)

    def get_height(self):
        return self.__height

    def calcArea(self):
        self.__area = self.__height * self.__width
        return self.__area

    def calcCircum(self):
        self.__circum = 2 * (self.__height + self.__width)
        return self.__circum

