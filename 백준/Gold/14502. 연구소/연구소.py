import copy
import sys
import itertools

# 지도 입력
n, m = map(int, sys.stdin.readline().split())
n_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# 0인 지점과 2인 지점을 구분 해서 저장
empty_list = []
virus_list = []
for i in range(n):
    for j in range(m):

        # 벽 조합 생성을 위해 저장
        if n_list[i][j] == 0:
            empty_list.append((i, j))
        # BFS알고리즘을 위해 저장
        elif n_list[i][j] == 2:
            virus_list.append((i, j))

# 모든 조합의 경우의 수 생성
max_cnt = 0
empty_combination_list = list(itertools.combinations(empty_list, 3))
for combination in empty_combination_list:

    # 연구소 지도 입력, deepcopy로 원본과 다른 개별적인 사본 생성
    n_copy_list = copy.deepcopy(n_list)

    # 가벽 위치 저장
    position1, position2, position3 = combination

    n_copy_list[position1[0]][position1[1]] = 1
    n_copy_list[position2[0]][position2[1]] = 1
    n_copy_list[position3[0]][position3[1]] = 1

    # 각 바이러스에 대해서 BFS 알고리즘 실행
    for default_virus_position in virus_list:

        queue_list = [default_virus_position]

        # BFS를 통해서 주변 0에 바이러스 전파
        while len(queue_list) != 0:

            virus_position = queue_list.pop(0)
            virus_x, virus_y = virus_position

            if virus_x - 1 != -1:
                if n_copy_list[virus_x - 1][virus_y] == 0:
                    n_copy_list[virus_x - 1][virus_y] = 2
                    queue_list.append((virus_x - 1, virus_y))
            if virus_x + 1 != n:
                if n_copy_list[virus_x + 1][virus_y] == 0:
                    n_copy_list[virus_x + 1][virus_y] = 2
                    queue_list.append((virus_x + 1, virus_y))
            if virus_y - 1 != -1:
                if n_copy_list[virus_x][virus_y - 1] == 0:
                    n_copy_list[virus_x][virus_y - 1] = 2
                    queue_list.append((virus_x, virus_y - 1))
            if virus_y + 1 != m:
                if n_copy_list[virus_x][virus_y + 1] == 0:
                    n_copy_list[virus_x][virus_y + 1] = 2
                    queue_list.append((virus_x, virus_y + 1))

    # 안전 구역 수 확인
    cnt = 0
    for i in range(n):
        for j in range(m):
            if n_copy_list[i][j] == 0:
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt
        max_list = n_copy_list

print(max_cnt)