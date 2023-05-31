import sys
from collections import deque

start_position, end_position = map(int, sys.stdin.readline().split())
position_list = [-1 for _ in range(0, 1000001)]
second = 0
min_second = -1

bfs_deque = deque([])

position_list[start_position] = second
bfs_deque.append((start_position, second))

while len(bfs_deque) != 0:

    position, second = bfs_deque.popleft()

    if position == end_position:
        if min_second == -1:
            min_second = second
        else:
            if second < min_second:
                min_second = second

    if position != end_position:
        if 0 <= position + 1 <= 100000:
            # 처음 접근 했다면
            if position_list[position + 1] == -1:
                position_list[position + 1] = second + 1
                bfs_deque.append((position + 1, second + 1))
            # 접근한 적 있다면
            else:
                if second + 1 < position_list[position + 1]:
                    position_list[position + 1] = second + 1
                    bfs_deque.append((position + 1, second + 1))
        if 0 <= position - 1 <= 100000:
            # 처음 접근 했다면
            if position_list[position - 1] == -1:
                position_list[position - 1] = second + 1
                bfs_deque.append((position - 1, second + 1))
            # 접근한 적 있다면
            else:
                if second + 1 < position_list[position - 1]:
                    position_list[position - 1] = second + 1
                    bfs_deque.append((position - 1, second + 1))
        if 0 <= position * 2 <= 100000:
            # 처음 접근 했다면
            if position_list[position * 2] == -1:
                position_list[position * 2] = second
                bfs_deque.append((position * 2, second))
            # 접근한 적 있다면
            else:
                if second < position_list[position * 2]:
                    position_list[position * 2] = second
                    bfs_deque.append((position * 2, second))

print(min_second)