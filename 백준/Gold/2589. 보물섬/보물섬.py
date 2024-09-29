import copy
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
n_list = []     # 지도의 정보를 저장
n_set = set()   # 이미 방문한 땅의 위치를 저장
land_list = []   # 땅의 위치를 저장
directions_info = [(1, 0),(-1, 0),(0, 1),(0, -1)]

# 지도 정보를 입력 받는다.
for i in range(n):
    n_list.append(list(sys.stdin.readline().strip()))

    # 지도의 정보 중에서 땅의 위치를 입력 받는다.
    for j in range(m):
        if n_list[i][j] == "L":
            land_list.append((i, j, 0))

# 각 땅의 위치별로 BFS 알고리즘을 진행해서 최대 거리를 구한다.
deque_a = deque()
max_cnt = 0
for land_x, land_y, land_cnt in land_list:

    # 이미 방문한 땅의 위치는 매번 초기화 한다.
    n_set = set()

    # deque n_set 초기값 정의
    deque_a.append((land_x, land_y, land_cnt))
    n_set.add((land_x, land_y))
    
    # BFS 알고리즘
    while len(deque_a) > 0:

        land_x, land_y, cnt = deque_a.popleft()
        max_cnt = max(max_cnt, cnt)

        # 현재 땅의 상하 좌우를 확인
        for dx, dy in directions_info:

            # 상하좌우 새로운 위치 저장
            nx, ny = land_x + dx, land_y + dy

            # 상하좌우 위치가 범위 안에 있는 경우
            if 0 <= nx < n and 0 <= ny < m:

                # 상하좌우가 땅이면서 이전에 방문한적 없는지 확인
                if n_list[nx][ny] == "L" and (nx, ny) not in n_set:

                    deque_a.append((nx, ny, cnt + 1))
                    n_set.add((nx, ny))

print(max_cnt)