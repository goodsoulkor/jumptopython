# 02-6 집합 자료형
# 만들기
s1 = set([1, 2, 3, 4])
print(s1)
s2 = set("hello")
print(s2)
s3 = set()
print(s3)
print()

# 집합 자료형의 특징
"""
- 중복을 허용하지 않는다.
- 순서가 없다.
순서가 없기 때문에 인덱싱 값을 얻을 수 없다.
인덱싱으로 접근하기 위해서는 리스트, 튜플로 변환해야 한다.
"""
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
print(l1[0])
t1 = list(s1)
print(t1)
print(t1[0])
print()
# 중복을 허용하지 않기 때문에 중복 제거를 위한 필터 역할로 종종 사용하기도 한다.

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 1. 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 2. 합집합
print(s1 | s2)
print(s1.union(s2))

# 3. 차집합
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))
print()

# 집합 자료형 관련 함수들
# 값 1개 추가하기 add
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러개 추가하기 update
s1.update([4, 5, 6])
print(s1)

# 특정값 제거하기 remove
s1.remove(4)
print(s1)
