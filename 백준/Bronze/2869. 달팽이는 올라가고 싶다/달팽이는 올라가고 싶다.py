import sys

sun, moon, height = map(int, sys.stdin.readline().split())

cnt = (height - sun) // (sun - moon)
remain = (height - sun) % (sun - moon)

# 딱 나누어 떨어지는 경우
if remain == 0:
    cnt += 1
else:
    cnt += 2

print(cnt)