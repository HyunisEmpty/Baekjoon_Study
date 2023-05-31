import sys
from collections import deque

start_position, end_position = map(int, sys.stdin.readline().split())
second = 0
min_second = -1

bfs_set = set()
bfs_deque = deque([])

bfs_set.add(start_position)
bfs_deque.append((start_position, second))

while len(bfs_deque) != 0:

    position, second = bfs_deque.popleft()

    if position == end_position:
        if min_second == -1:
            min_second = second
        else:
            if second < min_second:
                min_second = second

    # 현재 위치가 목적지라면 추가적인 연산을 하지 않는다.
    if position != end_position:
        if position + 1 not in bfs_set and 0 <= position + 1 <= 100000:
            bfs_deque.append((position + 1, second + 1))
            bfs_set.add(position + 1)
        if position - 1 not in bfs_set and 0 <= position - 1 <= 100000:
            bfs_deque.append((position - 1, second + 1))
            bfs_set.add(position - 1)
        if position * 2 not in bfs_set and 0 <= position * 2 <= 100000:
            bfs_deque.append((position * 2, second + 1))
            bfs_set.add(position * 2)

print(min_second)