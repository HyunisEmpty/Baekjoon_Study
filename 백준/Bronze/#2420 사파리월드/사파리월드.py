import sys 
n, m = map(int, sys.stdin.readline().split())

ans = n - m
if ans < 0:
    print(-ans)
else:
    print(ans)