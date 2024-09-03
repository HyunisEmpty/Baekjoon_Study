import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    n = int(sys.stdin.readline().strip())

    n_list = []
    for i in range(2):
        n_list.append(list(map(int, sys.stdin.readline().strip().split())))

    dp_list = [[0 for i in range(n + 1)] for j in range(2)]
    for i in range(n):

        ia = n_list[0][i]
        ib = n_list[1][i]

        # ia_next에 접근 하는 3개의 경우
        ia_1 = dp_list[0][i] # ia_next와 직선 상의 스티커를 사용하지 않는경우
        ia_2 = dp_list[1][i] # ia_next와 대각선 상의 스티커를 사용하지 않는경우
        ia_3 = dp_list[1][i] + n_list[1][i] # ia_next와 대각선 상의 스티커를 사용하는 경우

        # ia_next에 접근 하는 3개의 경우
        ib_1 = dp_list[1][i]  # ib_next와 직선 상의 스티커를 사용하지 않는경우
        ib_2 = dp_list[0][i]  # ib_next와 대각선 상의 스티커를 사용하지 않는경우
        ib_3 = dp_list[0][i] + n_list[0][i]  # ib_next와 대각선 상의 스티커를 사용하는 경우

        dp_list[0][i + 1] = max(ia_1, ia_2, ia_3)
        dp_list[1][i + 1] = max(ib_1, ib_2, ib_3)


    answer = max(dp_list[0][n], dp_list[1][n])
    print(answer)