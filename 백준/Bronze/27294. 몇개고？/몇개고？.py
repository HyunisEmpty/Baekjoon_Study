import sys

a, b = map(int, sys.stdin.readline().split())

if ( 12 <= a <= 16) and b == 0:
    print(320)
else:
    print(280)