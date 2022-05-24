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
