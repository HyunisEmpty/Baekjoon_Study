import sys

m = int(sys.stdin.readline().strip())
d = int(sys.stdin.readline().strip())

if m > 2:
    print("After")
elif m == 2:
    if d > 18:
        print("After")
    elif d == 18:
        print("Special")
    else:
        print("Before")
else:
    print("Before")