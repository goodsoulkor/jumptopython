# 03-1 if 문
# 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 쓰이는 if 문
# 돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다.
money = True
if money:
    print("Taxi")
else:
    print("Walk")
print()

# if 문의 기본 구조
"""
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
"""

# if 조건문: 바로 아래 문장부터 if 문에 속하는 모든 문장은 들여쓰기 해야 한다.

# 비교연산자
"""
x < y : x가 y보다 작다
x > y : x가 y보다 크다
x == y : x와 y가 같다
x != y : x와 y가 같지 않다
x >= y : x가 y보다 크거나 같다.
x <= y : x가 y보다 작거나 같다.
"""
x = 3
y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)
print()

# 만약 3000원 이상의 돈을 가지고 있다면 택시를 타고 그렇지 않으면 걸어가라.
money = 2000
if money >= 3000:
    print("Taxi")
else:
    print("Walk")
print()

# and, or, not
"""
x or y : x와 y 둘중 하나만 참이어도 참
x and y : x와 y 둘다 참이어야 참
not x : x가 거짓이면 참
"""
# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라.
money = 2000
card = True
if money >= 3000 or card:
    print("Taxi")
else:
    print("Walk")
print()

# x in s, x not in s
"""
x in 리스트 <> x not in 리스트
x in 튜플 <> x not in 튜플
x in 문자열 <> x not in 문자열
"""

a = [1, 2, 3]
print(1 in a)
print(1 not in a)
b = ("a", "b", "c")
print("a" in b)
c = "python"
print("j" in c)

# 만약 주머니에 돈이 있으면 택시를 타고 없으면 걸어가라
pocket = ["paper", "phone", "money"]
if "money" in pocket:
    print("Taxi")
else:
    print("Walk")
print()

# 조건문에서 아무일도 일어나지 않게 하고 싶다면
# 주머니에 돈이 있으면 가만히 있고 없으면 카드를 꺼내라
pocket = ["paper", "money", "phone"]
if "money" in pocket:
    pass
else:
    print("Card")
print()

# 다양한 조건을 만드는 elif
# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라
# if와 else 만으로 표현
pocket = ["paper", "phone"]
if "money" in pocket:
    print("Taxi")
else:
    if "card" in pocket:
        print("Taxi")
    else:
        print("Walk")

# 다중 조건 판단이 가능한 elif 사용
pocket = ["paper", "phone"]
if "money" in pocket:
    print("Taxi")
elif "card" in pocket:
    print("Taxi")
else:
    print("Walk")
print()

# if 문을 한 줄로 작성하기
# pocket = ["paper", "phone", "money"]
# if "money" in pocket: pass
# else: print("Card")

# 조건부 표현식
score = 75
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)
# 조건부 표현식으로 표현
message = "success" if score >= 60 else "failure"
print(message)
