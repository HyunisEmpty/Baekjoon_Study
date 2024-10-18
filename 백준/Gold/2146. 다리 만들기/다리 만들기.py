import sys
from collections import deque

n = int(sys.stdin.readline().strip())
n_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
n_visited = [[False for j in range(n)] for i in range(n)]

# 각 섬의 위치를 저장
island_list = []
island_queue = deque()
for ix in range(n):
    for iy in range(n):

        if n_list[ix][iy] == 1 and not n_visited[ix][iy]:   # 해당 위치가 육지며 방문하지 않은 경우
            island_set = set()
            island_queue.append((ix, iy))
            n_visited[ix][iy] = True

            while island_queue:     # 각 섬에 대해서 BFS 알고리즘 실행
                x, y = island_queue.popleft()
                island_set.add((x, y))

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if n_list[nx][ny] == 1 and not n_visited[nx][ny]:     # 주변 육지를 저장(한 섬안의 모든 육지 저장0
                            island_queue.append((nx, ny))
                            n_visited[nx][ny] = True

            island_list.append(island_set)      # 섬이 구분된 경우 해당 섬의 정보와 초기 위치를 저장

# for i in range(n):
#     print(n_visited[i])
#
# for i in range(len(island_list)):
#     print(island_list[i])

# 각 섬마다 주변 모든 섬에 다리를 연결하고 그 최솟값을 저장
min_bride = 201
bridge_queue = deque()
for island in island_list:

    bridge_list = [[0 for j in range(n)] for i in range(n)] # 시작 섬에서 출발한 다리의 최소 길이가 저장된는 리스트

    for island_info in island:      # 현재 섬의 모든 육지 정보를 받아 온다.
        is_x, is_y = island_info
        bridge_queue.append((is_x, is_y))

    while bridge_queue:
        x, y = bridge_queue.popleft()

        if bridge_list[x][y] <= min_bride:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:   # 상하좌우 접근
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:                 # 인덱스 범위 내부인지 판단

                    if n_list[nx][ny] == 0:                     # 만약 해당 타일이 바다 라면
                        if bridge_list[nx][ny] == 0:                # 만약 현재 바다에 접근한 것이 처음 이라면
                            bridge_list[nx][ny] = bridge_list[x][y] + 1
                            bridge_queue.append((nx, ny))
                        else:
                            if bridge_list[nx][ny] > bridge_list[x][y] + 1:
                                bridge_list[nx][ny] = bridge_list[x][y] + 1
                                bridge_queue.append((nx, ny))

                    elif n_list[nx][ny] == 1:                   # 만약 해당 타일이 육지 라면

                        if (nx, ny) in island:                  # 현재 섬이 시작 섬 이라면
                            pass
                        else:                                   # 현재 섬이 다른 섬 이라면
                            if min_bride > bridge_list[x][y]:       # 현재 까지 만들어진 다리의 길이가 최소라면
                                min_bride = bridge_list[x][y]

    # print("")
    # for i in range(len(bridge_list)):
    #     print(bridge_list[i])
print(min_bride)
