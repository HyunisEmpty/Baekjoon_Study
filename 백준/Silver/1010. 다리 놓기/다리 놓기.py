import sys
import math

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    n, m = map(int, sys.stdin.readline().strip().split())

    answer = int(math.factorial(m) / (math.factorial(m - n) * math.factorial(n)))

    print(answer)