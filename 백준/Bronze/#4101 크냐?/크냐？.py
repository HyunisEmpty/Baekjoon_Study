import sys

while True:
    a, b = map(int, sys.stdin.readline().split())

    if a + b != 0:
        if a > b:
            print("Yes")
        else:
            print("No")
    else:
        break