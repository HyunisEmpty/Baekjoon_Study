import sys

test_number = int(sys.stdin.readline().strip())

for test_count in range(test_number):
    a, b = map(int, sys.stdin.readline().split())

    print(a + b)