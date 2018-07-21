#
#
#   18.05.31
#   클래스 상속 (super -> 바로 직전에 상속시킨 부모)
#


class Animal:
    def __init__(self, name=""):
        print("test의 조부모")
        self.__name = name
    def eat(self):
        print("동물이 먹고 있습니다.")

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def testing(self):
        print("!!!")

class Dog(Animal):
    def __init__(self, name=""):
        super().__init__(name)
        
    def eat(self):
        print(self.getName() + "가 먹고 있습니다.")

class Cat(Animal):
    def __init__(self, name=""):
        print("test의 부모")
        super().__init__(name)
        
    def eat(self):
        print(self.getName() + "가 먹고 있습니다.")

class test(Cat):
    def __init__(self, name=""):
        super().__init__(name)         # 부모는 누구??  -> 직전에 상속시킨 부모. (Cat)
    def test_1(self):
        print(self.getName())
    def test_2(self):
        super().testing()

def main():
    dog1 = Dog("haggy")
    dog1.eat()
    
    cat1 = Cat("kitty")
    cat1.eat()


main()
    
