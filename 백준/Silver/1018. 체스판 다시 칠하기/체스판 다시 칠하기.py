import sys

row, column = map(int, sys.stdin.readline().split())

board = []
for count in range(row):
    board.append(list(map(str, sys.stdin.readline().strip())))

min_list = []
for count_yy in range(row - 7):
    for count_xx in range(column - 7):
        # 첫째 행이 W로 시작하는 경우
        w_start = 0
        b_start = 0
        for count_y in range(8):
            # 홀수 행에 대한 연산
            if count_y % 2 == 0:
                # print(board[count_y])
                # 홀수 열에 대한 연산
                for count_x in range(0, 8, 2):
                    if board[count_y + count_yy][count_x + count_xx] == "W":
                        b_start += 1
                    else:
                        w_start += 1
                # 짝수 열에 대한 연산
                for count_x in range(1, 8, 2):
                    if board[count_y + count_yy][count_x + count_xx] == "B":
                        b_start += 1
                    else:
                        w_start += 1
            # 짝수 행에 대한 연산
            elif count_y % 2 == 1:
                # print(board[count_y])
                # 홀수 열에 대한 연산
                for count_x in range(0, 8, 2):
                    if board[count_y + count_yy][count_x + count_xx] == "B":
                        b_start += 1
                    else:
                        w_start += 1
                # 짝수 열에 대한 연산
                for count_x in range(1, 8, 2):
                    if board[count_y + count_yy][count_x + count_xx] == "W":
                        b_start += 1
                    else:
                        w_start += 1
        min_list.append(b_start)
        min_list.append(w_start)

print(min(min_list))

