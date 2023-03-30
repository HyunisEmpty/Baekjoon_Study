import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    n = int(sys.stdin.readline().strip())
    note_1 = set(map(int, sys.stdin.readline().split()))

    m = int(sys.stdin.readline().strip())
    note_2 = list(map(int, sys.stdin.readline().split()))

    for num in note_2:
        if num in note_1:
            print(1)
        else:
            print(0)