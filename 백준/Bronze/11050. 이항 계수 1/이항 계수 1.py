import sys

n, k = map(int, sys.stdin.readline().split())
top = 1
for i in range(1, n + 1):
    top = i * top
bottom1 = 1
bottom2 = 1

if k == 0:
    bottom1 = 1
else:
    for i in range(1, k + 1):
        bottom1 = i * bottom1

if n - k == 0:
    bottom2 = 1
else:
    for i in range(1, n - k + 1):
        bottom2 = i * bottom2

# print(top//(bottom1 * bottom2))
print(int(top//(bottom1 * bottom2)))