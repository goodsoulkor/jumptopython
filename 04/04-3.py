# 04-3 파일 읽고 쓰기

# 파일 생성하기
# f = open("newfile.txt", "w")
# f.close()

# 파일열기모드
"""
r : 읽기
w : 쓰기
a : 추가하기
"""

# 파일을 쓰기 모드로 열어 출력값 적기
# f = open("newfile.txt", "w")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# 프로그램 외부에 저장된 파일을 읽는 여려가지 방법
# readline 함수
# f = open("./newfile.txt", "r")
# line = f.readline()
# print(line)
# f.close()

# f = open("./newfile.txt", "r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()

# readlines 함수 이용하기
# f = open("newfile.txt", "r")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# 줄바꿈 문자 제거
# strip 사용
# f = open("newfile.txt", "r")
# lines = f.readlines()
# for line in lines:
#     line = line.strip()
#     print(line)
# f.close()

# read 함수 사용
# f = open("newfile.txt", "r")
# data = f.read()
# print(data)
# f.close()

# 파일에 새로운 내용 추가하기
# f = open("newfile.txt", "a")
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# with 문과 함께 사용
# 자동으로 파일객체를 닫는다
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
