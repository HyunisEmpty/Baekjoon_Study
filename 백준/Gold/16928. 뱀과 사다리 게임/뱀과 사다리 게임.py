import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [100 for i in range(101)]
board[1] = 0

nm_dict = dict()
for i in range(n + m):
    key, val = map(int, sys.stdin.readline().split())
    nm_dict[key] = val

queue = deque()
queue.append(1)
while queue:

    now_position = queue.popleft()
    # print(now_position, board)
    for dice_number in range(1, 7):
        future_position = now_position + dice_number
        if 1 <= future_position <= 100:
            if future_position in nm_dict:      # 주사위의 도착 지점이 사다리 혹은 뱀인 경우
                # print(now_position, future_position, nm_dict[future_position])
                if board[nm_dict[future_position]] > board[now_position] + 1:
                    # print(future_position, nm_dict[future_position])
                    board[future_position] = board[now_position] + 1
                    board[nm_dict[future_position]] = board[now_position] + 1
                    queue.append(nm_dict[future_position])      # 사다리 혹은 뱀의 도착 위치 저장
            else:
                if board[future_position] > board[now_position] + 1:
                    board[future_position] = board[now_position] + 1
                    queue.append(future_position)               # 주사위를 돌려 도착할 위치 저장

print(board[len(board) - 1])