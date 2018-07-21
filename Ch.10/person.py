#
#
#   18.05.17
#   내장함수를 이용한 리스트 정렬
#

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<이름: %s, 나이: %s>" % (self.name, self.age)

def keyAge(person):
    return person.age

people = [Person("홍길동", 20), Person("김철수", 35), Person("최자영", 38)]
print(sorted(people, key = keyAge)) # 나이 오름차순
print(sorted(people, key = keyAge, reverse = True)) # 나이 내림차순

print(sorted(people, key = lambda person : person.name))    # 키값으로 람다함수 이용
print(sorted(people, key = lambda person : person.age))
print(sorted(people, key = lambda person : person.name, reverse = True))
print(sorted(people, key = lambda person : person.age, reverse = True))

