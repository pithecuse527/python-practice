class MyCounter(object):
    #생성자 메소드 정의.
    def __init__(self, low, high):
        self.__current = low
        self.__high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current > self.__high:
            raise StopIteration
        else:
            self.__current += 1
            self.__current -= 1
            return self.__current

def MyCounterGen(low, high):
    while low <= high:
        yield low
        low += 1
        
for i in MyCounterGen(1, 10):
    print(i, end=' ')

print()
c = MyCounter(1, 10)
for i in c:
    print(i, end=' ')

