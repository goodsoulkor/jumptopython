# 02-5 딕셔너리 자료형
# 딕셔너리?
"""
이름 = 홍길동, 생일 = 몇 월 며칠 등으로 대응관계를 나타내는 자료형을
파이썬에서는 딕셔너리라고 한다.
다른 언어에서는 연관 배열 또는 해시(Hash) 자료형이라고 한다.
파이썬에서는 Key: Value의 형태로 나타낸다.
"""

# 만들기
"""
기본 형태
{Key1: Value1, Key2: Value2, Key3: Value3, ...}
* Key에는 변하지 않는 값을 사용하고 Value에는 변하지 않는 값, 변하는 값 모두를 사용할 수 있다.
"""
# ex
dic = {"name": "goodsoul", "phone": "01029332772", "birth": "0612"}

# key로 정수 값 1, value로 문자열 "hi"를 사용
a = {1: "hi"}
# value에 리스트를 넣을 수도 있다.
a = {"a": [1, 2, 3]}

# 딕셔너리 쌍 추가, 삭제하기
a = {1: "a"}
a[2] = "b"
print(a)
a["name"] = "goodsoul"
print(a)
a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제하기
del a[1]
print(a)

# key를 사용해 value 얻기
grade = {"goodsoul": 99, "james": 10}
print(grade["goodsoul"])
print(grade["james"])
print()

# 딕셔너리 생성 시 주의사항
"""
딕셔너리에서 key의 값은 고유한 값이므로 중복되는 key값을 설정해 놓으면 하나를 제외한 나머지 모두 무시된다.
"""
a = {1: "a", 1: "b"}
print(a)
print()

# 딕셔너리 관련 함수들
# key 리스트 만들기 keys
a = {"name": "goodsoul", "phone": "01029332772", "birth": "0612"}
print(a.keys())
"""
a.keys()는 딕셔너리 a의 key만 모아서 dict_keys 객체를 돌려준다.
dict_keys 객체는 다음과 같이 사용할 수 있다.
리스트를 사용하는 것과 차이가 없지만 리스트 고유의 함수 append, insert, pop, remove, sort 등은 사용할 수 없다.
"""
for k in a.keys():
    print(k)

# dict_keys 객체를 리스트로 변환하려면 다음과 같다.
a_list = list(a.keys())
print(a_list)
print()

# value 리스트 만들기 values
print(a.values())

# key, value 쌍 얻기 items
print(a.items())
# items 함수는 key, value 쌍을 튜플로 묶은 dict_items 객체를 돌려준다.

# key, value 쌍 모두 지우기 clear
a.clear()
print(a)
print()

# key로 value 얻기 get
a = {"name": "goodsoul", "phone": "01029332772", "birth": "0612"}
print(a.get("name"))
print(a.get("phone"))
# key가 없는 경우에는 None을 돌려준다.
print(a.get("com"))
# key가 없을 경우 디폴트 값을 대신 가져오게 하고 싶을 때
print(a.get("come", "없음"))
print()

# 해당 키가 딕셔너리 안에 있는지 확인 in
print("name" in a)
print("com" in a)
