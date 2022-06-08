# 05-5 내장 함수

# abs
# abs(x)는 입력 받은 숫자의 절대값을 돌려준다.
from ast import Lambda


print(abs(3))
print(abs(-3))
print(abs(-1.2))
print()

# all
# all(x)는 반복 가능한 자료형 x를 입력받아 x의 모든 요소가 참이면 True, 하나라도 거짓이면 False를 돌려준다.
print(all([1, 2, 3]))
print(all([0, 1, 2, 3]))
print(all([]))
print()
# 빈 값이 인수로 주어지면 True를 리턴한다.

# any
# any(x)는 반복 가능한 자료형 x를 입력받아 x의 요소 중 하나라도 참이 있으면 True, 모두 거짓이면 False를 리턴한다.
print(any([1, 2, 3, 4, 0]))
print(any([0, ""]))
print(any([]))
print()
# 빈 값이 인수로 주어지면 False를 리턴한다.

# chr
# chr(i)는 유니코드 값을 입력받아 그 코드에 해당하는 문자를 리턴한다.
print(chr(97))
print(chr(44032))
print()

# dir
# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
print(dir([1, 2, 3]))
print(dir({"1": "a", "2": "b"}))
print()

# divmod
# divmod(a, b)는 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려준다.
print(divmod(4, 2))
print()

# enumerate
# enumerate는 순서가 있는 자료형(리스트, 튜플, 문자열)을 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
for i, name in enumerate(["body", "foo", "bar"]):
    print(i, name)
print()

# eval
# eval(expresion)은 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 값을 돌려준다.
print(eval("1+2"))
print(eval("'hi'+'a'"))
print(eval("divmod(4, 3)"))
print()

# filter
# filter(f, iterable)는 입력받은 함수에 입력받은 반복가능한 자료형의 요소값이 차례로 입력되었을 때 반환 값이 참인 것만 묶어서 돌려준다.
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result


print(positive([1, -3, 2, 0, -5, 6]))

# filter 사용
def positive2(x):
    return x > 0


print(list(filter(positive2, [1, -3, 2, 0, -5, 6])))

# lambda를 사용하면 더 간략하게 표현가능
result = list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
print(result)
print()

# hex
# hex(x)는 정수값을 입력 받아 16진수로 변환하여 돌려준다.
print(hex(234))
print(hex(3))
print()

# id
# id(object)는 객체를 입력 받아 객체의 고유 주소를 돌려주는 함수이다.
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
print()

# input
# input([prompt])는 사용자 입력을 받는 함수이다.
# a = input()
# b = input("enter : ")

# int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자등을 정수 형태로 돌려주는 함수이다.
a = int("3")
b = int(3.14)
print(a, b)
# 2진수로 표현된 11의 10진수 값
c = int("11", 2)
print(c)
# 16진수로 표현된 1A의 10진수 값
d = int("1A", 16)
print(d)
print()

# isinstance
# isinstance(object, class) 입력 받은 오브젝트가 입력 받은 클래스의 인스턴스 인지 판별한다.
class Person:
    pass


a = Person()
print(isinstance(a, Person))
b = 3
print(isinstance(b, Person))
print()

# len
# len(s)는 입력값 s의 길이를 반환한다.
print(len("python"))
print(len([1, 2, 3]))
print(len((1, "a")))
print()

# list
# list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려준다.
print(list("python"))
print(list([1, 2, 3]))
a = [1, 2, 3]
b = list(a)
print(b)
print()
# list함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.

# map
# map(f, iterable) 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려준다.
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result


result = two_times([1, 2, 3, 4])
print(result)

# map 사용
def two_times2(x):
    return x * 2


result2 = list(map(two_times2, [1, 2, 3, 4]))
print(result2)

# lambda를 사용하여 더 간단하게
result3 = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(result3)
print()

# max
# max(iterable)은 반복 가능한 자료형에서 최대값을 돌려준다.
print(max([1, 2, 3]))
print(max("python"))
print()

# min
# min(iterable)은 반복 가능한 자료형에서 최소값을 돌려준다.
print(min([1, 2, 3, 4]))
print(min("python"))
print()

# oct
# oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려준다.
print(oct(34))
print(oct(1234))
print()

# open
# open(filename, [mode])은 파일이름과 읽기 방법을 입력받아 파일 객체를 돌려준다. 읽기 방법을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 준다.
"""
w : 쓰기모드
r : 일기모드
a : 추가모드
b : 바이너리모드
"""
# f = open("binary_file", "rb")

# ord
# ord(c)는 문자의 유니코드 값을 돌려준다.
print(ord("a"))
print(ord("가"))
print()

# pow
# pow(a, b) a의 b제곱 값을 돌려준다.
print(pow(3, 2))
print()

# range
# range([start,] stop [,step])는 입력 받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.
print(list(range(5)))
# 시작 숫자를 지정하지 않으면 0부터 시작한다

print(list(range(5, 10)))
# 시작과 끝이 주어졌을 경우 끝 숫자는 포함되지 않는다.

print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))
print()
# 인수가 3개인 경우 마지막 인수는 숫자 사이의 거리를 말한다.

# round
# round(number[,ndigits]) 숫자를 입력받아 반올림 해준다.
print(round(4.5))
print(round(4.2))
print(round(3.141592, 2))
# 두 번째 인수는 반올림하여 표시하고 싶은 소수점의 자리수 이다.
print()

# sorted
# sorted(iterable)는 입력값을 정렬한 후 그 결과를 리스트로 돌려준다.
print(sorted([3, 2, 1, 4]))
print(sorted(("b", "c", "a")))
print(sorted("zero"))
print()

# str
# str(object)는 문자열 형태로 객체를 변환하여 돌려준다.
print(str(3))
print(str("hi"))
print(str("hi".upper()))
print()

# sum
# sum(iterable)은 입력받은 리스트나 튜플의 모든 요소값의 합을 돌려준다.
print(sum([1, 2, 3, 4]))
print(sum((1, 2, 3, 4)))
print()

# tuple
# tuple(iterable)은 반복 가능한 자료형을 받아 튜플로 만들어 준다.
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))
print(tuple("abc"))
print()

# type
# type(object)는 입력값의 자료형이 무엇인지 알려준다.
print(type("abc"))
print(type([]))
# print(type(open("test", "w")))
print()

# zip
# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 준다
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))
