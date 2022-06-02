# 불 자료형
# 불 자료형이란?
"""
불(bool) 자료형이란 참(True)과 거짓(False)를 나타내는 자료형이다. 불 자료형은 다음 두 가지 값만 가질 수 있다.
- True
- False
True나 False는 예약어로 항상 첫 문자를 대문자로 작성한다.
"""
a = True
b = False
print(type(a))
print(type(b))
print()

# 조건문의 반환값
print(1 == 1)
print(2 > 1)
print(2 < 1)
print()

# a가 참인 경우 a.pop()을 계속 실행
a = [1, 2, 3, 4]
while a:
    print(a.pop())

print()

if []:
    print("참")
else:
    print("거짓")

if [1, 2, 3]:
    print("참")
else:
    print("거짓")

print()

# 불 연산
# bool 내장 함수를 사용하여 자료형의 참과 거짓을 식별할 수 있다.
print(bool("python"))
print(bool(""))
print(bool([1, 2, 3]))
print(bool([]))
print(bool(0))
print(bool(3))
