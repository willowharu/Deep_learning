# Magic Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(iterator), 함수(Functions), 클래스(Class)
# 클래스안에 정의 할 수 있는 특별한(Built-in) 메소드

#class example 2
# vector(x, y), (5, 2)
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# Max((5, 10)) = 10 

class Vector(object):
    '''
    example:  Vector.__doc__
    '''

    def __init__(self, *args): #args -> packing gotj epdlxj sjarla
        '''
        Create a vector, example : v = Vector(5, 10)
        '''
        if len(args) == 0:
            self.x, self.y = 0, 0
        else:
            self.x, self.y = args
    
    def __repr__(self):
        ''' Return the vector information'''
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __add__(self, other):
        ''' Return the vector addtion of self and other'''
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, y):
        ''' Return the vector addtion of self and other'''
        return Vector(self.x * y, self.y * y)

    def __bool__(self):
        if self.x == 0 and self.y == 0:
            print("Warining")
            return bool(max(self.x, self.y))

        else:
            return bool(max(self.x, self.y))


# vector instance  generation
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()
# v5 = Vector(23, 35, 29, 12)
# print(Vector.__doc__)
# print(Vector.__init__.__doc__)

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1*3)
print(v2*20)

print(bool(v1), bool(v2))
print(bool(v3))