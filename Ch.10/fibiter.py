class FibIterator:
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a
        self.b = b
        self.maxValue = maxValue
        
    def __iter__(self):
        return self
    
    def __next__(self):
        n = self.a + self.b
        if n > self.maxValue:
            raise StopIteration()
        self.a = self.b
        self.b = n
        return n

def fibGenerator(a=1, b=0, maxValue=50):
    n = 0
    while True:
        n = a+b
        a = b
        b = n
        if n < maxValue:
            yield n
        else:
            break
        
for i in fibGenerator():
    print(i, end=" ")
