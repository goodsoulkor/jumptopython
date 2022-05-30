# 문자열 자료형

# 문자열 만들기
# 1. 큰따옴표
a = "Hello World"

# 2. 작은 따옴표(자동 포맷팅 되어 큰따옴표로 변환)
b = "Hello World"

# 3. 큰따옴표 3개
c = """헬로 월드"""

# 4. 작은따옴표 3개(자동 포맷팅 되어 큰따옴표로 변환)
d = """Life is too short, You need Python"""

# 문자열 안에 작은따옴표나 큰따옴표 포함
# 1. 작은따옴표 포함
food = "Python's favorite food is perl"
print(food)
print()

# 2. 큰따옴표 포함
say = '"Python is very easy." he says.'
print(say)
print()

# 3. 백슬래시를 사용
# food = 'Python\'s favorite food is perl'
# say = "\"Python is very easy.\" he says."

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1. 줄바꿈 이스케이프 코드 \n 삽입
multiline = "Life is too short\nYou need python"
print(multiline)
print()

# 2. 연속된 따옴표 사용
multiline = """
Life is too short
You need python
"""
print(multiline)
print()

# multiline = '''
# Life is too short
# You need python
# '''

# 자주쓰이는 이스케이프 문자
# \n : 줄바꿈
# \t : 탭간격
# \\ : 문자 \를 그대로 표현
# \', \"

# 문자열 연산하기
# 문자열 더하기
head = "Python"
tail = " is fun!"
print(head + tail)

# 문자열 곱하기
a = "Python"
print(a * 2)
print()

# 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열의 길이 구하기
a = "Life is too short"
print(len(a))
print()

# 문자열 인덱싱과 슬라이싱
# 문자열 인덱싱?
a = "Life is too short, You need Python"
print(a[3])

# 인덱싱 활용
print(a[0])
print(a[12])
print(a[-1])
print(a[-2])
print(a[-5])
print()

# 문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
# 0 <= a < 4
print(a[0:5])
print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])  # 19 <= a < -7

# 슬라이싱으로 문자열 나누기
a = "20220524Clear"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
year = a[:4]
day = a[4:8]
print(year)
print(day)
print()

# Pithon을 Python으로 바꾸기
a = "Pithon"
print(a[:1])
print(a[2:])
print(a[:1] + "y" + a[2:])
print()

# 문자열 포매팅
# 1. 숫자 바로 대입
print("I eat %d apples." % 3)

# 2. 문자열 바로 대입
print("I eat %s apples." % "five")

# 3. 숫자를 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

# 문자열 포맷 코드
# %s : 문자열(string)
# %c : 문자 1개(character)
# %d : 정수(integer)
# %f : 부동소수(floating-point)
# %o : 8진수
# %x : 16진수
# %% : Literal %(문자 % 자제)

print("I have %s apples" % 3)
print("rate is %s" % 3.234)

# 포매팅 연산자와 %를 함께 사용
print("Error is %d%%" % 98)

# 포맷 코드와 숫자 함께 사용하기
# 1. 정렬과 공백
print("%10s" % "hi")
print("%-10s" % "hi")

# 2. 소수점 표현하기
print("%0.4f" % 3.14125839)
print("%10.4f" % 3.141215)
print()

# format 함수를 사용한 포매팅
# 숫자 바로 대입
print("I eat {0} apples.".format(3))

# 문자열 바로 대입
print("I eat {0} apples.".format("five"))

# 숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples.".format(number))

# 두 개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

# 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

# 인덱스와 이름 혼용
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
print()

# 왼쪽 정렬
print("{0:<10}".format("hi"))

# 오른쪽 정렬
print("{0:>10}".format("hi"))

# 가운데 정렬
print("{0:^10}".format("hi"))

# 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# 소수점 표현하기
y = 3.141592
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

# { 또는 } 표현하기
print("{{ and }}".format())
print()

# f 문자열 포매팅
# 파이썬 3.6 부터 가능
name = "홍길동"
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}살 입니다.")
print(f"나는 내년에 {age+1}살이 된다.")

# 딕셔너리
d = {"name": "홍길동", "age": 30}
print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다.")

# 정렬
print(f"{'hi':=^10}")
print(f"{'hi':!<10}")

# 소수점
y = 3.141592
print(f"{y:0.4f}")
print(f"{y:10.4f}")

# { }
print(f"{{ and }}")
print()

# 문자열 관련 함수
# 문자 개수 세기 count
a = "hobby"
print(a.count("b"))

# 위치 알려주기1 find
# 처음 나온 위치를 알려주고 없으면 -1을 반환한다.
a = "Python is the best choice"
print(a.find("b"))
print(a.find("k"))

# 위치 알려주기2 index
# 없으면 오류 발생한다.
a = "Life is too shrot"
print(a.index("t"))
# print(a.index("k"))

# 문자열 삽입 join
print(",".join("abcd"))
print(",".join(["a", "b", "c", "d"]))

# 소문자를 대문자로 바꾸기 upper
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기 lstrip
a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기 rstrip
a = " hi "
print(a.rstrip())

# 양쪽 공백 지우기 strip
a = " hi "
print(a.strip())

# 문자열 바꾸기 replace
a = "Life is too shrot"
print(a.replace("Life", "Your leg"))

# 문자열 나누기 split
# 아무값도 없는 경우 공백을 기준으로 문자열을 나누어준다.
# 특정 값을 입력한 경우 그 값을 구분자로 나누어 준다.
a = "Life is too shrot"
print(a.split())
b = "a:b:c:d"
print(b.split(":"))
