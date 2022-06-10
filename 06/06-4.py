# 간단한 메모장 프로그램
# 옵션에 따라 메모를 저장하고 출력하는 메모장
# -a : 입력옵션 / -v 출력옵션
import sys

option = sys.argv[1]

if option == "-a":
    memo = sys.argv[2]
    f = open("memo.txt", "a")
    f.write(memo)
    f.write("\n")
    f.close()
elif option == "-v":
    f = open("memo.txt", "r")
    memo = f.read()
    f.close()
    print(memo)
