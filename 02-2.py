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
