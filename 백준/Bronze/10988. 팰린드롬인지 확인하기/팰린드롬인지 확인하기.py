import sys

word = sys.stdin.readline().strip()

if word == word[::-1]:
    print(1)
else:
    print(0)