# Magic Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(iterator), 함수(Functions), 클래스(Class)
# 클래스안에 정의 할 수 있는 특별한(Built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# "모든 객체 -> id", "type -> value"

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1])**2)
print(l_leng1)

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt4)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y)**2)
print(l_leng2)


# 네임드 튜플 선언
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) #Default = False


# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# print
print(Point1, Point2, Point3, Point4)

p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

#usage
print(p1[0] + p2[1])
print(p1.x + p2.y)

# unpacking
x, y = p2
print(x, y)

# namedtuple method
temp = [52, 38]
# _make(): new object generation
p4 = Point1._make(temp)
print(p4)

# _field: fieid name ghkrdls
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderDict return ***
print(p1._asdict())