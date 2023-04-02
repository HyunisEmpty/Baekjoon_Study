import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    count = i + 1
    print(" " * (n-count) + "*" * (count))