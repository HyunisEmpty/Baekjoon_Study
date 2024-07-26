import sys

n, test_case = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0] * (n + 1)

for i in range(1, n + 1):

    sum_list[i] = sum_list[i - 1] + n_list[i - 1]

for test in range(test_case):

    # i번째 수 부터 J번째 수 까지의 합
    i, j = map(int, sys.stdin.readline().split())

    print(sum_list[j] - sum_list[i-1])

