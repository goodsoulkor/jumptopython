# 04-1 함수

# 파이썬 함수의 구조
"""
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
"""


from ast import Lambda


def add(a, b):
    return a + b


a = 3
b = 4
c = add(a, b)
print(c)
print()

# 매개변수와 인수
"""
매개변수(parameter)와 인수(arguments)는 혼용해서 사용되는 헷갈리는 용어이다.
매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고 인수는 함수를 호출할 때 입력값을 말한다.
"""


def add(a, b):  # a, b는 매개변수
    return a + b


print(add(3, 4))  # 3, 4는 인수
print()

# 입력값과 결과값에 따른 함수의 형태
# 1. 일반적인 함수 - 입력값이 있고 결과값이 있는 함수
def add(a, b):
    result = a + b
    return result


a = add(3, 4)
print(a)
print()

# 2. 입력값이 없는 함수
def say():
    return "HI"


a = say()
print(a)
print()

# 3. 결과값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))


add(3, 4)
print()

# 4. 입력값도 결과값도 없는 함수
def say():
    print("HI")


say()
print()

# 매개변수 지정하여 호출하기
# 매개변수를 지정하면 순서에 상관없이 사용할 수 있다.
def add(a, b):
    return a + b


result = add(a=3, b=4)
print(result)

result2 = add(b=4, a=3)
print(result2)
print()

# 입력값이 여려개일 경우
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result


result = add_many(1, 2, 3)
print(result)
result2 = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result2)
print()


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result


result = add_mul("add", 1, 2, 3, 4, 5)
result2 = add_mul("mul", 1, 2, 3, 4, 5)
print(result, result2)
print()

# 키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)
print_kwargs(name="goodsoul", age=42)
print()
# 키워드 파라미터를 사용하면 딕셔너리가 된다.

# 함수의 결과 값은 언제나 하나이다.
def add_and_mul(a, b):
    return a + b, a * b


result = add_and_mul(3, 4)
print(result)
a, b = add_and_mul(3, 4)
print(a, b)
print()

# return의 또다른 쓰임새
# 특별한 상황에서 함수를 빠져나가고 싶을 때 return을 사용한다.
def say_nick(nick):
    if nick == "babo":
        return
    print("My nickaname is %s" % nick)


say_nick("goodsoul")
say_nick("babo")
print()

# 매개변수에 초기값 미리 설정하기
def say_myself(name, old, man=True):
    print("My name is %s" % name)
    print("I'm %d old" % old)
    if man:
        print("I'm man")
    else:
        print("I'm woman")


say_myself("goodsoul", 42)
say_myself("goodsoul", 42, True)
say_myself("goodsoul", 42, False)
print()

# 함수 안에서 선언한 변수의 효력 범위
a = 1


def vartest(a):
    a += 1


vartest(a)
print(a)
print()
# 함수 안에서 사용된 변수와 밖에서 사용된 변수는 다르다.

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용(권장)
a = 1


def vartest(a):
    a += 1
    return a


a = vartest(a)
print(a)

# 2. global 사용하기
a = 1


def vartest():
    global a
    a += 1


vartest()
print(a)
print()

# lambda
add = lambda a, b: a + b
result = add(3, 4)
print(result)
