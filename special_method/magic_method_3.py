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