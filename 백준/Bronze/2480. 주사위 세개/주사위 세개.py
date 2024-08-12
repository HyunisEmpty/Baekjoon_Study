import sys

a, b, c = map(int, sys.stdin.readline().strip().split())

if a == b and b == c:
    print(10000 + a * 1000)
elif a == b:
    print(a * 100 + 1000)
elif b == c:
    print(b * 100 + 1000)
elif c == a:
    print(c * 100 + 1000)
else:
    print(max(a, b, c) * 100)