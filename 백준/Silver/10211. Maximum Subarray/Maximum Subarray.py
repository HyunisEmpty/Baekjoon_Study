import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    n = int(sys.stdin.readline().strip())
    sum_list = [0] + list(map(int, sys.stdin.readline().strip().split()))

    max_sub = 0
    max_bool = True

    # 누적 합 연산
    for i in range(1, n + 1):
        sum_list[i] += sum_list[i - 1]

    for i in range(n + 1):

        for j in range(i, n + 1):

            if i != j:
                if max_bool:
                    max_sub = sum_list[j] - sum_list[i]
                    max_bool = False
                else:
                    if sum_list[j] - sum_list[i] > max_sub:
                        max_sub = sum_list[j] - sum_list[i]

    print(max_sub)