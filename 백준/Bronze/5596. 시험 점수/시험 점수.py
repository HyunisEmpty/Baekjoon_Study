import sys

a = sum(list(map(int, sys.stdin.readline().split())))
b = sum(list(map(int, sys.stdin.readline().split())))

print(max(a, b))
