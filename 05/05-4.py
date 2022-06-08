# 05-4 예외처리

# 오류 발생
# f = open("newfile", "r")
# f.close()

# print(4 / 0)

# a = [1, 2, 3]
# print(a[4])

# try, except 문을 이용한 오류 예외 처리 기법
"""
try:
    ...
except [발생 오류 [as 오류 메시지 변수]]:
    ...
"""

# 오류 예외 처리 3가지 방법
# 1. try, except만 쓰는 방법
"""
try:
    ...
except:
    ...
"""
# 오류 종류에 상관없이 오류가 발생하면 except 구문이 실행된다.

# 2. 발생한 오류만 포함한 except문
"""
try:
    ...
except 발생 오류:
    ...
"""
# 오류가 발생했을 때 except문에 지정된 오류와 일치할 때만 except 블록을 수행한다.

# 3. 발생 오류와 오류메시지 변수까지 포함한 except문
"""
try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...
"""
# 오류 메시지의 내용까지 알고 싶을 때 사용한다.
# ex
# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)

# try .. finally
# finally 절은 try문 수행 중 예외 발생 여부와 상관없이 언제나 실행된다.
# 리소스를 close해야 할 때 많이 사용한다.
# f = open("newfile", "r")
# try:
#     data = f.read()
# finally:
#     f.close()

# 여러개 오류 처리하기
# try:
#     a = [1, 2]
#     print(a[3])
#     4 / 0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱 할 수 없습니다.")

# 오류 메시지 가져오기
# try:
#     a = [1, 2]
#     print(a[3])
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)

# 오류 두 개 함께 처리
# try:
#     a = [1, 2]
#     print(a[3])
#     4 / 0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)

# try문에 else절 사용하기
# try:
#     age = int(input("나이를 입력하세요: "))
# except:
#     print("입력이 정확하지 않습니다.")
# else:
#     if age <= 18:
#         print("미성년자는 출입금지입니다.")
#     else:
#         print("환영합니다.")

# 오류 회피하기
# try:
#     f = open("newfile", "r")
# except FileNotFoundError:
#     pass

# 일부러 오류 발생 시키기

# Bird 클래스를 상속 받을 때 fly 메서드를 구현하지 않으면 오류 발생
# class Bird:
#     def fly(self):
#         raise NotImplementedError


# class Eagle(Bird):
#     pass


# eagle = Eagle()
# eagle.fly()

# 오류 발생하지 않으려면 Bird를 상속 받을 때 fly 메서드 구현
# class Bird:
#     def fly(self):
#         raise NotImplementedError


# class Eagle(Bird):
#     def fly(self):
#         print("very fast")


# eagle = Eagle()
# eagle.fly()

# 예외 만들기
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."


def say_nick(nick):
    if nick == "babo":
        raise MyError()
    print(nick)


# say_nick("angel")
# say_nick("babo")

# 예외 처리 기법으로
# try:
#     say_nick("angel")
#     say_nick("babo")
# except MyError:
#     print("허용되지 않는 별명입니다.")

# 오류 메시지 사용
try:
    say_nick("angel")
    say_nick("babo")
except MyError as e:
    print(e)
# 메시지가 출력되기 위해서는
# class MyError(Exception):
#     def __str__(self):
#         return "허용되지 않는 별명입니다."
