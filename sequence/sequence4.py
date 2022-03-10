# 해시테이블(hashtable) → 적은 리소스를 통해서 많은 데이터를 효율적 관리
# dict → key 중복 허용 X, Set → 중복 허용 X
# dict 및 set 추가

# immutable dict

from re import M
from types import MappingProxyType

d = {'key1': 'value1'}


# Read only
d_frozen = MappingProxyType(d)

print(d_frozen)
#d는 수정이 가능하고 d_frozen은 수정이 불가능

print(d, id(d))
print(d_frozen, id(d_frozen))

# print(d, id(d), hash(d))
# print(d_frozen, id(d_frozen), hash(d_frozen))

# 수정가능
d['key2'] = 'value2'
print(d)

# 수정불가능
# d_frozen['key2'] = 'value2'
print(d)




s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'kiwi'])
s3 = {3}
s4 = set() # Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'kiwi'})
print(type(s4))
# 추가 가능
s1.add('Melon')
print(s1)
# 추가 불가
# s5.add('Melon') # 중요한 값들은  얼려버려서...값들은 보존..

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 바이트 코드 실행 → 파이썬 인터프리터 실행
from dis import dis
print('------')
print(dis('{10}'))
print('------')
print(dis('set([10])'))

# {}, set을 비교하면 위에꺼는 3단계로 구성되고 아래것은 과정이 더많다.. 그래서 집합을 활용할때는,.{} 이게 더 좋다...
