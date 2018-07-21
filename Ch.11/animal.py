class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return '?'

class Dog(Animal):
    def __init__(self,name2):
        super().__init__(name2)
        self.name2 = name2
    
    def speak(self):
        return '멍멍!'

class Cat(Animal):
    def speak(self):
        return '야옹!'
