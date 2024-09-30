import sys
import itertools
import copy
from collections import deque

n, virus_count = map(int, sys.stdin.readline().split())

# 기존 지도와 동일한 형태의 지도 생성(지도내 최댓값을 구하기 위해), 빈칸(0) => -1 벽(1) => -2
n_list = []     # 개선된 지도의 정보를 저장
virus_list = [] # 바이러스를 설치 가능한 위치를 저장
for i in range(n):
    n_list.append([])
    map_info = list(sys.stdin.readline().split())
    for j in range(n):
        # 빈 칸인 경우
        if map_info[j] == "0":
            n_list[i].append(-1)
        # 벽인 경우
        elif map_info[j] == "1":
            n_list[i].append(-2)
        # 바이러스인 경우
        elif map_info[j] == "2":
            virus_list.append((i, j, 0))
            n_list[i].append(-1)

# 바이러스를 설치 가능한 곧의 조합을 생성
virus_combinations_list = list(itertools.combinations(virus_list, virus_count))

# 각 조합 마다 바이러스에 대해서 BFS 알고리즘 실행
deque = deque()     # BFS 알고리즘을 위한 큐 자료구조
direction_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]     # 상하좌우 접근을 위한 리스트
min_time = -1
min_list = []
for virus_combination in virus_combinations_list:

    # 현재 지도의 사본 저장
    n_deepcopy_list = copy.deepcopy(n_list)

    # M개의 위치에 대해서 BFS 알고리즘 실행
    for i in range(virus_count):
        virus_x, virus_y, virus_cnt = virus_combination[i]
        n_deepcopy_list[virus_x][virus_y] = virus_cnt
        deque.append((virus_x, virus_y, virus_cnt))

        while len(deque) > 0:

            virus_x, virus_y, virus_cnt = deque.popleft()

            # 상하좌우 접근
            for direction in direction_list:

                dx, dy = direction

                # 상하좌우가 인덱스 범위 내부 인지
                if 0 <= virus_x + dx < n and 0 <= virus_y + dy < n:

                    # 상하좌우의 값이 현재 바이러스가 확장될때의 시간보다 큰 경우 혹은 초기값인 경우
                    if n_deepcopy_list[virus_x + dx][virus_y + dy] > virus_cnt + 1 or n_deepcopy_list[virus_x + dx][virus_y + dy] == -1:
                        n_deepcopy_list[virus_x + dx][virus_y + dy] = virus_cnt + 1
                        deque.append((virus_x + dx, virus_y + dy, virus_cnt + 1))

    # 모든 빈 칸에 바이러스가 있게 되는 최소 시간 저장, 지도 내에 -1이 존재 한다면 연산 중단
    flag = False
    now_max_time = -1
    for i in range(n):

        if flag:
            now_max_time = -1
            break

        for j in range(n):

            # 바이러스가 전체에 퍼지지 못한 경우
            if n_deepcopy_list[i][j] == -1:
                flag = True
                break

            if n_deepcopy_list[i][j] > now_max_time:
                now_max_time = n_deepcopy_list[i][j]

    # 만약에 지도에 -1이 없다면
    if flag == False:

        if min_time == -1:
            min_time = now_max_time
        else:
            if now_max_time < min_time:
                min_time = now_max_time
                min_list = copy.deepcopy(n_deepcopy_list)


print(min_time)
