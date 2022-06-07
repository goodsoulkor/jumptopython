# 04 연습문제

# Q1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
# def is_odd(num):
#     if num % 2 == 0:
#         return "짝수"
#     else:
#         return "홀수"


# print(is_odd(2))

# Q2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
# def num_average(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total / len(args)


# print(num_average(5, 5))

# Q3. 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다. 오류를 수정하자.
# input1 = input("첫번째 숫자를 입력하세요: ")
# input2 = input("두번째 숫자를 입력하세요: ")

# total = int(input1) + int(input2)
# print("두 숫자의 합은 %s 입니다." % total)

# Q4. 다음 중 출력 결과가 다른 것 한 개를 골라 보자.
# print("you" "need" "python")
# print("you" + "need" + "python")
# print("you", "need", "python")  # 쉼표를 사용하면 한 칸씩 띄어진다.
# print("".join(["you", "need", "python"]))

# Q5. "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램을 만들자
# with open("test.txt", "w") as f:
#     f.write("Life is too short")

# with open("test.txt", "r") as f2:
#     data = f2.read()
#     print(data)

# Q6. 사용자의 입력을 파일(test1.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

# with open("./test1.txt", "a") as f:
#     data = input("Input data :\n") + "\n"
#     f.write(data)

# Q7. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# with open("./test.txt", "r") as f:
#     data = f.read()

# with open("./test.txt", "w") as f2:
#     data2 = data.replace("java", "python")
#     f2.write(data2)
