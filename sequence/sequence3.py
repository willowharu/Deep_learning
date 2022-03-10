# 해시테이블
# 해시테이블 키가 중복 되었을때, 처리 방법..?
# 해시테이블 이란 ..? key에 value를 저장하는 구조…
# 키를 통해서 데이터가 저장되기때문에 키가 중복되면 안됨…
# 파이썬 dict 해쉬 테이블 예임…
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조..
# key값을 해싱 함수를 통해서 해쉬 주소 값이 나오고.. 이 주소 값을 기반으로 키에 대한 value를 참조 할 수 있음..
# hash table 검색해보기


# hash 

# hash 값 확인
from hashlib import new
from operator import ne


t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) #list가 mutable 형태라 ...해쉬 함수를 사용못함
#해쉬함수를 사용하기 위해서 immutable 이어야한다

#  Dict set default example
# 사용하는것을 권장… 속도가 빠름..
source = (('k1', 'val1'), 
          ('k1', 'val2'), 
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5)')       
        )
# dictionary로 만들기..

new_dict1 = {}
new_dict2 = {}
# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)
# use setdefautl
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)
