# 게시판 페이징 만들기

# 게시물 총 건수와 페이지당 보여줄 게시물 수를 입력 받아 총 페이지 수를 구하는 프로그램


def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1


print(getTotalPage(5, 10))
print(getTotalPage(20, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
