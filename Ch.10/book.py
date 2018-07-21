class Book:
    title = ''
    pages = 0

    def __init__(self, title='', pages=0):
        self.__title = title
        self.__pages = pages

    def __str__(self):
        return self.__title

    def __add__(self, other):
        return self.__pages + other.__pages
    
book1 = Book('자료구조', 600)
book2 = Book('C언어', 700)
a = book1 + book2

print(a)
