import sys
from collections import deque

start_position, end_position = map(int, sys.stdin.readline().split())
position_list = [-1 for _ in range(0, 1000001)]
second = 0
min_second = -1
bfs_deque = deque([])
position_list[start_position] = second
bfs_deque.append((start_position, second))


def NewPosition(new_position, new_second):
    if 0 <= new_position <= 100000:
        # 처음 접근 했다면
        if position_list[new_position] == -1:
            position_list[new_position] = new_second
            bfs_deque.append((new_position, new_second))
        # 접근한 적 있다면
        else:
            if new_second < position_list[new_position]:
                position_list[new_position] = new_second
                bfs_deque.append((new_position, new_second))
    

while len(bfs_deque) != 0:

    position, second = bfs_deque.popleft()

    if position == end_position:
        if min_second == -1:
            min_second = second
        else:
            if second < min_second:
                min_second = second

    if position != end_position:
        NewPosition(position + 1, second + 1)
        NewPosition(position - 1, second + 1)
        NewPosition(position * 2, second)

print(min_second)