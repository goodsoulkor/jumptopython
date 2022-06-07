# 05-1 클래스

# 클래스 만들기
# 더하는 계산기 구현
# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result


# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(2))
# print(cal2.add(5))

# 클래스와 객체
class Cookie:
    pass


a = Cookie()
b = Cookie()
# a, b는 Cookie 클래스로 만든 객체이다
# a, b는 Cookie의 인스턴스인다.

# 사직연산 클래스 만들기
class FourCal:
    # 생성자 만들기 -> 객체에 초기값을 설정해야 할 필요가 있을 때 만든다
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):  # 객체의 계산할 숫자를 지정할 수 있다.
        self.first = first
        self.second = second

    # 더하기 기능
    def add(self):
        result = self.first + self.second
        return result

    # 곱하기 기능
    def mul(self):
        result = self.first * self.second
        return result

    # 빼기 기능
    def sub(self):
        result = self.first - self.second
        return result

    # 나누기 기능
    def div(self):
        result = self.first / self.second
        return result


# a = FourCal()
# a.setdata(4, 2)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())
# a = FourCal(4, 2)
# print(a.add())

# 클래스 상속
# FourCal 클래스를 상속하는 MoreFourCal 클래스
class MoreFourCal(FourCal):
    # 제곱 기능 추가
    def pow(self):
        result = self.first**self.second
        return result


# a = MoreFourCal(4, 2)
# print(a.pow())
# print(a.add())
# 상속은 기존 클래스는 그대로 놔두고 기능을 확장시킬 수 있다.

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


# a = SafeFourCal(4, 0)
# print(a.div())
# 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것 이렇게 하면 오버라이딩 한 메서드를 호출한다.

# 클래스 변수
class Family:
    lastname = "Kim"


print(Family.lastname)
# 클래스 안에 선언한 변수를 클래스 변수라고 한다.
# 해당 클래스로 만든 객체에서도 사용할 수 있다.
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

a.lastname = "Park"
print(Family.lastname)
print(a.lastname)
print(b.lastname)
