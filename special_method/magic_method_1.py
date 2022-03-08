# Magic Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(iterator), 함수(Functions), 클래스(Class)
# 클래스안에 정의 할 수 있는 특별한(Built-in) 메소드

#기본형
# print(int(10))
# print(int)
# print(float) 

#모든 속성 및 메소드 출력
# print(dir(int))
# print(dir(float))

# n = 10 
# print(n +100)
# print(n.__add__(100))
# print(n.__doc__)
# print(n.__bool__(), bool(n))


#class example 1
class Fruit:
    def __init__(self, name, price):
        self.name = name #instance variable
        self.price = price #instance variable

    def __str__(self):
        return f'Fruit class info : {self.name}, {self.price}'

    def __add__(self, x):
        print('called >> __add__')
        return self.price + x.price
    def __sub__(self, x):
        print('Called >> __sub__')
        return self.price - x.price
    def __le__(self, x):
        print('Caleed >> __le__')
        if self.price <= x.price:
            return True
        else:
            return False
    def __ge__(self, x):
        print('Caleed >> __ge__')
        if self.price >= x.price:
            return True
        else:
            return False


# instance  generation
instance1 = Fruit("Orange", 7500)
instance2 = Fruit('Banana', 3500)

print(instance1 + instance2)
#general computation
# print(instance1.price + instance2.price)

#magic method
print(instance1 >= instance2)
print(instance1 <= instance2)
print(instance1 - instance2)
print(instance2 >= instance1)
print(instance1)
print(instance2 )