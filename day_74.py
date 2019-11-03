#-------- DAY 74 "exercise1" --------
# 1. Read a file
# f = open("exerFile.txt", "x")
# f = open("exerFile.txt", "r")
# for x in f:
#     print(x)
# f.close()
f = open("exerFile.txt", "a")
f.write("The best way we learn anything is by practice and exercise questions")
f.close()
f = open("exerFile.txt", "r")
for x in f:
    print(x)
f.close()
