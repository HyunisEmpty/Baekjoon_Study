import sys

h, m = map(int, sys.stdin.readline().split())

cnt = 0
while cnt < 45:

    if m != 0:
        m -= 1
    else: ## 00분인 경우
        m = 59
        if h != 0:
            h -= 1
        else:
            h = 23

    cnt += 1

print(h, m)