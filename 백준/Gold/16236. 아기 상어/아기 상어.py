import sys
import copy
from collections import deque

sea_size = int(sys.stdin.readline().strip())
sea_list = [list(map(int, sys.stdin.readline().strip().split())) for i in range(sea_size)]
visited = [[False for y in range(sea_size)] for x in range(sea_size)]

# 상어 정보 저장
shark_size = 2
distance = 0
shark_position = 0
for x in range(sea_size):
    for y in range(sea_size):
        if sea_list[x][y] == 9:
            sea_list[x][y] = 0
            shark_position = (x, y, distance, shark_size)

# 아기 상어가 사냥 가능한 물고기가 없을때 까지 반복
queue = deque()
mom_help_flag = False   # 엄마의 도움을 받았는지 확인
total_distance = 0      # 사냥에 총 이동한 거리 저장(소요한 시간과 동일)
shark_grow_up = 0
while not mom_help_flag:    # 엄마의 도움을 안받은 경우 실행

    # print()
    # for i in range(sea_size):
    #     print(sea_list[i])

    mom_help_flag = True    # 이번 연산에 엄마의 도움을 받는지 확인
    queue.append(shark_position)
    copy_visited = copy.deepcopy(visited)

    prey_min_distance = -1
    prey_list = []

    # 현재 상어가 사냥 가능한 사냥감을찾는 BFS 알고리즘
    while queue:

        x, y, distance, shark_size = queue.popleft()

        # 상하좌우 접근
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < sea_size and 0 <= ny < sea_size) and (not copy_visited[nx][ny]):   # 인덱스 범위 내이며 접근한 적 없는지 판단
                if 0 <= sea_list[nx][ny] <= shark_size: # 상어가 이동 가능한 경우

                    # 사냥감이 있든 없든 이동
                    queue.append((nx, ny, distance + 1, shark_size))
                    copy_visited[nx][ny] = True

                    if 0 < sea_list[nx][ny] < shark_size: # 사냥 가능한 경우

                        mom_help_flag = False   # 사냥을 할 수 있기에 엄마의 도움을 받지 않았다.

                        if prey_min_distance == distance + 1:   # 현재 사냥감 과의 거리가 최소 거리와 같다면
                            prey_list.append((nx, ny))
                        else:
                            if prey_min_distance == -1 or distance + 1 < prey_min_distance: # 현재 사냥감 과의 거리가 최소 라면
                                prey_min_distance = distance + 1
                                prey_list = [(nx, ny)]

    # print("prey min distance", prey_min_distance)
    # print("shark size", shark_grow_up, shark_size)

    # 사냥 가능한 사냥감이 있다면
    if prey_list:

        # 높이를 기준으로 오름차순 정렬 높이가 같다면 y를 기준으로 오름차순 정렬
        prey_list = sorted(prey_list, key=lambda x: (x[0], x[1]))
        # print("now sort", prey_list)

        min_x, min_y = prey_list[0]             # 가장 가까운 물고기 위치 저장및 사냥
        sea_list[min_x][min_y] = 0              # 사냥을 했으므로 지도에서 사냥감 제거
        total_distance += prey_min_distance     # 사냥에 소요된 시간 저장

        shark_grow_up += 1                      # 사냥에 성공 했으므로 현재 상어 성장
        if shark_grow_up == shark_size:         # 샤크 성장 판단
            shark_size += 1
            shark_grow_up = 0

        shark_position = (min_x, min_y, 0, shark_size)  # 상어 위치, 크기 초기화

print(total_distance)
