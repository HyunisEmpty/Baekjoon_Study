import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):
    input = sys.stdin.readline().strip()
    print(input[0] + input[len(input) - 1])