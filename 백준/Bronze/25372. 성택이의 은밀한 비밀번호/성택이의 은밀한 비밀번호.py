import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    password = sys.stdin.readline().strip()

    if 6 <= len(password) <= 9:
        print("yes")
    else:
        print("no")