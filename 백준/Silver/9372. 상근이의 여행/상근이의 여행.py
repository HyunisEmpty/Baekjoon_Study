import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):
    node_count, line_count = map(int, sys.stdin.readline().split())

    carrier = ""
    for i in range(line_count):
        carrier = sys.stdin.readline().strip()

    print(node_count-1)