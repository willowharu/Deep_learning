# Magic Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(iterator), 함수(Functions), 클래스(Class)
# 클래스안에 정의 할 수 있는 특별한(Built-in) 메소드

#기본형
print(int(10))
print(int)
print(float) 

#모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10 
print(n +100)
print(n.__add__(100))
print(n.__doc__)
print(n.__bool__(), bool(n))