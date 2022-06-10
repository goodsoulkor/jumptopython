# 06-6 하위 디렉터리 검색
# 특정 디렉터리부터 시작해서 그 하위 모든 파일 중 파이썬 파일만 출력해주는 프로그램
import os


# def search(dirname):
#     try:
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename)
#             if os.path.isdir(full_filename):
#                 search(full_filename)
#             else:
#                 ext = os.path.splitext(full_filename)[-1]
#                 if ext == ".py":
#                     print(full_filename)
#     except PermissionError:
#         pass


# search("./")

for (path, dir, files) in os.walk("./"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == ".py":
            if dir == []:
                print("%s/%s" % (path, filename))
            else:
                print("%s%s" % (path, filename))
