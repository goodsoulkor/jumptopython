# 04-2 사용자 입력과 출력

# 사용자 입력
# input의 사용
# a = input()
# print(a)

# 프롬프트를 띄워 사용자 입력 받기
# number = input("input number: ")
# print(number)

# print 자세히 알기
# 1. 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다
print("Life" "is" "too short")
print("Life" + "is" + "too short")
print()

# 2. 문자열 띄어쓰기는 콤마로 한다.
print("life", "is", "too short")
print()

# 3. 한 줄에 결과값 출력하기
for i in range(10):
    print(i, end=" ")
