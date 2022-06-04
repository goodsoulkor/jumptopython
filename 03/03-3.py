# 03-3 for문

# for문의 기본 구조
"""
for 변수 in 반복가능한 객체(리스트, 튜플, 문자열):
    수행할 문장1
    수행할 문장2
"""

# 전형적인 for문
# test_list = ["one", "two", "three"]
# for i in test_list:
#     print(i)

# 다양한 for 문의 사용
# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#     print(first + last)

# for문의 응용
# "총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오."
# marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks:
#     number += 1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# for문과 continue
# marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks:
#     number += 1
#     if mark < 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % number)

# for문과 함께 자주 사용하는 range 함수
a = range(10)
print(a)
print()

a = range(1, 11)
print(a)
print()

# range함수 예시
# 1부터 10의 합을 구하라
add = 0
for i in range(1, 11):
    add += i

print(add)
print()

# 60점 이상 합격
# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] < 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

# for와 range를 이용한 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")
#     print()

# 리스트 내포 사용하기
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

print(result)

b = [1, 2, 3, 4]
result2 = [num * 3 for num in b]
print(result2)

# 짝수만 3 곱하기 : 조건문 추가
result3 = [num * 3 for num in b if num % 2 == 0]
print(result3)

# 리스트 내포에서 for 문을 여려개 사용할 수 있다.
# 구구단의 결과를 리스트에 저장
result4 = [x * y for x in range(2, 10) for y in range(1, 10)]
print(result4)
