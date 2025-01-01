import sys

n = 0

for _ in range(4):

    n += int(sys.stdin.readline().strip())

print(n//60)
print(n%60)