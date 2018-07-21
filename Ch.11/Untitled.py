class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None
'''
    def getName(self):
        return self.__name
        
    def getPet(self):
        return self.__pet
'''

dog1 = Dog("흰둥이")
person1 = Person("짱구")
person1.pet = dog1

print(person1.name + "의 애완동물 이름은 " + person1.pet.name + "이다.")
