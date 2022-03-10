# sequence
# container(서로다른 자료형을 저장하는 것[list, tuple, collections.deque])
# flat (단일 자료형만 저장 가능 [str, bytes, bytearray, array.array, memoryview] / 이게 필요한 순간 .. 조금이라도 속도를 빠르게 하고 싶다... 내가 저장하고자 하는 데이터를 데이터 타입에 맞춰서 저장)
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)


# 지능형 리스트(comprehending list)
chars = '#_)(*&^%$#@!'

code_list1 = list()

for s in chars:
    # unicod list
    code_list1.append(ord(s))

print(code_list1)

# comprehending lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

# comprehending lists + Map, filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
print(code_list4) 

print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4]) 


# Generator 생성 및 장점 찾아보기
# 한 번에 한개의 항목을 생성(메모리 유지X)
import array

tuple_g = [ord(s) for s in chars]
tuple_g1 = (ord(s) for s in chars)
array_g = array.array("I", (ord(s) for s in chars))
print(tuple_g)
print(next(tuple_g1))
print(next(tuple_g1))
print(next(tuple_g1))

print(array_g)


# 제너레이터 예제
print(('%s' % c + str(n) for c in ['A' 'B', 'C', 'D'] for n in range(1 ,21)))

for s in ('%s' % c + str(n) for c in ['A' 'B', 'C', 'D'] for n in range(1 ,21)):
    print(s)



# 리스트할때 주의할 점
marks1 = [['~'] * 3 for _ in range(4)] # id 값이 첫번째것으로 사용한거는 정화하게 복사가 되어서 모두 다 다른  리스트 아이디 값이 주소값이 다 다른것이고 
marks2 = [['~'] * 3] * 4 # 하나의 주소값이 4개가 복사가 된거라 수정이 이뤄지는 것임

print(marks1)
print(marks2)

print()

marks1[0][1] = 'x'
marks2[0][1] = 'x'

print(marks1)
print(marks2)

# prove 데이터가 이상하다..그럼 id값을 찍어봐라..
print([id(i) for i in marks1])
print([id(i) for i in marks2])