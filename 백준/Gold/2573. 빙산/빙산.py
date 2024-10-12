import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ice_queue = deque()
iceberg_queue = deque()
iceberg_set = set()
update_ice = deque()

# queue에 현재 모든 빙산의 위치를 저장한다.
for x in range(n):
    for y in range(m):
        if n_list[x][y] >= 1:   # 빙산 이라면
            ice_queue.append((x, y, n_list[x][y]))

day = 0
iceberg_split = False       # 빙산이 나뉘어 졌는지 판단
no_ice = False
while not iceberg_split and not no_ice:    # 모든 연산은 빙산이 분리되기 전까지 반복한다.

    ice_cnt = len(ice_queue)
    for i in range(ice_cnt):     # 모든 얼음에 대해 상하좌우 물이 있는지 판단
        x, y, ice_size = ice_queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if n_list[nx][ny] == 0 and ice_size > 0:    # 상하좌우 값이 바다 라면
                    ice_size -= 1                       # 물의 개수 만큼 현재 빙산 -1

        update_ice.append((x, y, ice_size))
        if ice_size != 0:       # 빙산의 값이 0이 되었다면 제거
            ice_queue.append((x, y, ice_size))

    while update_ice: # 지도 업데이트
        x, y, size = update_ice.popleft()
        n_list[x][y] = size

    day += 1        # 빙산에 대한 연산이 끝났으므로 년도가 1증가 한다.

    if len(ice_queue) != 0:
        # 빙산이 분리 되었음을 판단하기 queue에 임의의 값을 받아와 BFS 알고리즘의 초기값으로 설정하고 연산을 진행한다.
        iceberg_queue.append(ice_queue[0])
        iceberg_set.clear()
        iceberg_set.add(ice_queue[0])
        while iceberg_queue:

            x, y, ice_size = iceberg_queue.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m: # 현재 얼음의 상하좌우에 얼음이 있는지 판단
                    if (nx, ny, n_list[nx][ny]) not in iceberg_set and n_list[nx][ny] != 0:
                        iceberg_queue.append((nx, ny, n_list[nx][ny]))
                        iceberg_set.add((nx, ny, n_list[nx][ny]))

        if len(ice_queue) != len(iceberg_set):  # 빙산이 분리 됬다면
            iceberg_split = True

    else:   # 지도에 더이상 얼음이 없다면
        no_ice = True

if no_ice:
    print(0)
else:
    print(day)
