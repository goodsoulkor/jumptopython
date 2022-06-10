# 구구단 출력
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i += 1
    return result


print(GuGu(2))
