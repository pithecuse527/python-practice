class Vehicle:
    def __init__(self, make, model, color, price):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__price = price

    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    def getDesc(self):
        return "차량 = (" + str(self.__make) + ", " +\
               str(self.__model) + ", " +\
               str(self.__color) + ", " +\
               str(self.__price) + ")"
    
