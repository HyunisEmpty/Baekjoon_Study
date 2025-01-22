import heapq
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

heap = deque()          # 힙 자료 구조
map_list = []           # 지도 정보를 저장
cheese_set = set()      # 치즈 위치를 저장
del_cheese_set = set()  # 지워야할 치즈 위치를 저장
for i in range(N):

    map_list.append(list(map(int, sys.stdin.readline().split())))

    for j in range(M):  # 치즈 위치 저장
        if map_list[i][j] == 1:
            cheese_set.add((i,j))

day = 0
while len(cheese_set) != 0:     # 치즈가 남아있는 경우

    heap.append((0, 0))
    cnt_list = [[0 for _ in range(M)] for _ in range(N)]    # 치즈인 경우 노출된 면의 수 저장
    visited_list = [[False for _ in range(M)] for _ in range(N)]    # 방문 여부 저장
    visited_list[0][0] = True  # 방문여부 저장

    # BFS 알고리즘
    while heap:

        x, y = heap.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:   # 상하좌우 접근
            nx, ny = x + dx, y + dy     # 새로운 좌표 생성
            if 0 <= nx < N and 0 <= ny < M:

                if map_list[nx][ny] == 1:   # 치즈인 경우

                    cnt_list[nx][ny] += 1

                    if cnt_list[nx][ny] >= 2:   # 공기랑 2면 이상 접하는 치즈인 경우

                        del_cheese_set.add((nx, ny))

                else:   # 공기인 경우

                    if not visited_list[nx][ny]:    # 방문하지 않는 경우
                        heap.append((nx, ny))
                        visited_list[nx][ny] = True

    # print("")
    # for i in range(N):
    #     print(map_list[i])

    for cx, cy in del_cheese_set:
        if (cx, cy) in cheese_set:
            cheese_set.remove((cx, cy))
        map_list[cx][cy] = 0    # 지도에서 치즈를 제거

    day += 1

print(day)