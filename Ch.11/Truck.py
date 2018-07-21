from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, make, model, color, price, payload):
        super().__init__(make, model, color, price)
        self.__payload = payload

    def setPayload(self, payload):      # setter
        self.__payload = payload
        
    def getPayload(self):               # getter
        return self.__payload

    def getDesc(self):
        return self.__payload

def main():
    myTruck = Truck("Tesla", "Model S", "white", 10000, 2000)
    myTruck.setMake("Tesla")
    myTruck.setPayload(2000)
    print(myTruck.getDesc())

main()
