# sequence2
# container(서로다른 자료형을 저장하는 것[list, tuple, collections.deque])
# flat (단일 자료형만 저장 가능 [str, bytes, bytearray, array.array, memoryview] / 이게 필요한 순간 .. 조금이라도 속도를 빠르게 하고 싶다... 내가 저장하고자 하는 데이터를 데이터 타입에 맞춰서 저장)
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)


# Tuple Advanced
# Unpacking

# b, a = a, b

from audioop import reverse


print(divmod(100, 9))
# print(divmod((100,9))) error -> need to make unpacking
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = 1,2,3,4,5
print(x, y, rest)

# muatble / immutable
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2 # id값이 달라짐… l을 재할당 하는 것..
m = m * 2 # id값이 달라짐… l을 재할당 하는 것..
print(l, id(l))
print(m, id(m))


l *= 2 
m *= 2 
print(l, id(l)) #튜플 한 번 저장이 되면 값 수정이 안되기 때문에, 새로운 주소 받음…(아이디 재할당..)
print(m, id(m))# 가변형이라.. 원래 아이디에 그대로 받음


# sorted : 정렬 후 새로운 객체 반환
# sort : 정렬 후 객체 직접 변경

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - ', sorted(f_list, key=lambda x: x[-1]))
print('sorted - ', sorted(f_list, key=lambda x: x[-1], reverse=True))
print('sorted - ', sorted(f_list))

# sort : 정렬 후 객체 직접 변경


# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list)



# list vs array 적합한 사용법 설명
# 리스트 기반: 융통성...(다양한 데이터 타입을 담을 수  있음.. 범용적 사용)
# 숫자 기반은 array 활용