# 06-5 탭을 4개의 공백으로 바꾸기

# 문서파일을 읽어서 그 문서 파일 안에 있는 탭을 공백 4개로 바꾸는 스크립트
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " " * 4)

f = open(dst, "w")
f.write(space_content)
f.close()
