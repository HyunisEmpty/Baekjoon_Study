import sys
from collections import deque

start_position, end_position = map(int, sys.stdin.readline().split())
position_list = [-1 for _ in range(0, 1000001)]


def NewPosition(new_position, new_second):

    global position_list
    global bfs_deque

    # 인덱스 범위 확인
    if 0 <= new_position <= 100000:
        # 처음 접근 했다면
        if position_list[new_position] == -1:
            position_list[new_position] = new_second
            bfs_deque.append((new_position, new_second))
        # 접근한 적 있다면
        else:
            if new_second <= position_list[new_position]:
                position_list[new_position] = new_second
                bfs_deque.append((new_position, new_second))


# BFS 알고리즘 => 최단 시간 연산
min_second = abs(end_position - start_position)
bfs_deque = deque([])
min_cnt = 0
position_list[start_position] = 0
bfs_deque.append((start_position, position_list[start_position]))
while len(bfs_deque) > 0:

    position, second = bfs_deque.popleft()

    # 목적지 노드에 도착한 경우
    if position == end_position:
        if second < min_second:
            min_second = second
            min_cnt = 1
        elif second == min_second:
            min_cnt += 1
    else:
        NewPosition(position + 1, second + 1)
        NewPosition(position - 1, second + 1)
        NewPosition(position * 2, second + 1)

print(min_second, min_cnt)