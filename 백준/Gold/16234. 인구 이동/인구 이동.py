import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
n_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]   # 모든 도시의 위치와 인구를 저장
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
population_movement = True  # 이전 연산에서 인구 이동이 발생 했는지를 확인
queue = deque()

# 이전에 인구 이동이 발생했는지 확인
cnt_day = -1
while population_movement:

    population_movement = False
    cnt_day += 1 # 인구 이동이 며칠동안 발생했는지 확인

    n_visited = [[False for i in range(n)] for j in range(n)]  # 방문 여부 초기화

    # 모든 나라를 한번씩 방문
    for x in range(n):
        for y in range(n):

            # 현재 나라를 이전에 방문했는지 확인
            if n_visited[x][y] == False:

                # 현재 나라에 대해서 BFS 알고리즘 실행
                queue.append((x, y))
                n_visited[x][y] = True

                # 연합 생성 시작 (BFS 알고리즘 실행)
                union_cnt = 1   # 연합에 속한 국가 수 저장
                union_population = n_list[x][y]    # 연합에 속한 인구 저장
                union_country_list = [(x, y)]     # 연합에 속한 나라의 위치 저장
                while len(queue) > 0:

                    # 현재 나라의 위치를 받아 온다. 또한, 현재 나라를 방문 했다고 기록
                    dx, dy = queue.popleft()

                    # 상하좌우 나라에 접근
                    for delta_x, delta_y in directions:
                        nx, ny = delta_x + dx, delta_y + dy

                        # 인덱스 범위 안인지 국경 개방이 가능한 인구 차이며 이전에 방문한적 없는지 확인
                        if 0 <= nx < n and 0 <= ny < n:
                            if l <= abs(n_list[nx][ny] - n_list[dx][dy]) <= r and n_visited[nx][ny] == False:
                                n_visited[nx][ny] = True
                                queue.append((nx, ny))

                                # 연합에 속한 나라의 수, 총인구, 나라의 위치 저장
                                union_cnt += 1
                                union_population += n_list[nx][ny]
                                union_country_list.append((nx, ny))

                # 만약 연합에 속한 국가 2개 이상이라면 인구 이동 시작
                new_population = union_population//union_cnt
                if union_cnt >= 2:
                    population_movement = True
                    for ux, uy in union_country_list:
                        n_list[ux][uy] = new_population


print(cnt_day)


