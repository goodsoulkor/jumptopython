# 02-8 변수
# 변수 만들기
# 변수 이름 = 변수에 저장할 값
a = 1
b = "python"
c = [1, 2, 3]

# 변수란 객체를 가리키는 것이라고도 할 수 있다. 객체란 자료형과 같은 것을 의미한다.
a = [1, 2, 3]
# [1, 2, 3] 값을 가지는 리스트 자료형(객체)이 자동으로 메모리에 생성되고 변수 a는 리스트가 저장된 메모리의 주소를 가리키게 된다.
a = [1, 2, 3]
print(id(a))
print()

# 리스트를 복사하고 싶을 때
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)
# a와 b는 가리키는 대상이 동일하다.
a[1] = 4
print(a)
print(b)
print()

# b변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 하는 방법
# 1. [:] 이용
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)
print()

# copy 모듈 이용
from copy import copy

a = [1, 2, 3]
b = copy(a)
print(b is a)
print()

# 변수를 만드는 여러가지 방법
a, b = ("python", "life")
print(a)
print(b)
(a, b) = "python", "life"
print(a, b)
[a, b] = ["python", "life"]
print(a, b)
a = b = "python"
print(a, b)
print(id(a))
print(id(b))
print()

# 두 변수의 값을 바꾸는 방법
a = 3
b = 5
a, b = b, a
print(a)
print(b)
