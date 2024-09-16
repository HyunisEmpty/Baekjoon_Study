import sys

h, m = map(int, sys.stdin.readline().split())

answer = (h - 9) * 60 + m
print(answer)