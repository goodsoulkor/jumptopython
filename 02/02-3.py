# 리스트 자료형
# 리스트 만들기
odd = [1, 3, 5, 7, 9]
a = []
b = [1, 2, 3]
c = ["Life", "is", "too", "short"]
d = [1, 2, [3, 4]]
e = [1, 2, "Life", "is"]
f = list()

# 리스트의 인덱싱과 슬라이싱
# 인덱싱
a = [1, 2, 3]
print(a[0])
print(a[-1])

# 슬라이싱
print(a[:2])
print(a[1:])

# 이중 삼중 리스트 인덱싱, 슬라이싱
a = [1, 2, [3, 4, [5, 6]]]
print(a[2][0])
print(a[2][1:])
print(a[2][2][0])
print()

# 리스트 연산하기
# 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 리스트 반복
print(a * 2)

# 리스트 길이구하기
print(len(a))
print()

# 리스트 수정과 삭제
# 값 수정하기
a = [1, 2, 3]
a[2] = 0
print(a)

# del 함수로 요소 삭제하기
a = [1, 2, 3]
del a[0]
print(a)

b = [1, 2, 3, 4, 5, 6]
del b[:3]
print(b)
print()

# 리스트 관련 함수
# 요소 추가 append
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])
print(a)

# 정렬 sort
b = [3, 4, 2, 1]
b.sort()
print(b)

c = ["a", "d", "b", "c"]
c.sort()
print(c)
print()

# 뒤집기 reverse
d = [1, 3, 2, 4]
d.reverse()
print(d)

# 위치반환 index
a = [1, 2, 3]
print(a.index(3))
print()

# 요소 삽입 insert
a = [1, 2, 3]
a.insert(1, 4)
print(a)

# 요소제거 remove
a = [1, 2, 3, 4]
a.remove(2)
print(a)
b = [1, 2, 3, 4, 3]
b.remove(3)
print(b)
print()

# 요소 꺼내기 pop
a = [1, 2, 3, 4]
print(a.pop(1))
print(a)

# 요소 갯수 세기 count
a = [1, 2, 3, 3, 4]
print(a.count(3))

# 확장 extend
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)

b = [1, 2, 3]
b += [4, 5]
print(b)
