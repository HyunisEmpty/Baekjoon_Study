import sys

name_list = list(map(str, sys.stdin.readline().split("-")))

answer = ""
for name in name_list:
    answer += name[0]

print(answer)