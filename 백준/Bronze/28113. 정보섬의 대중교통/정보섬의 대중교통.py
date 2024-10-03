import sys

b2, a, b = map(int, sys.stdin.readline().split())

if a > b:
    print("Subway")
elif a < b:
    print("Bus")
elif a == b:
    print("Anything")