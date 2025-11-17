import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# 지도 정보 저장
map_list = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 각 빈칸이 속한 영역의 번호를 저장하는 배열
area_map = [[-1] * m for _ in range(n)]

# 영역별 크기를 저장하는 리스트
area_size_list = []

# 방문 배열
visited = [[False] * m for _ in range(n)]

# 이동 벡터 정의 (상, 하, 좌, 우)
move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

area_index = 0  # 영역 번호


def bfs(sx, sy):
    """
    빈칸(0) 기준으로 BFS를 수행하여 연결된 영역을 찾는다.
    해당 영역의 모든 칸에 동일한 영역번호를 부여한다.
    """
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True
    area_map[sx][sy] = area_index

    cnt = 1  # 현재 영역 크기

    while queue:
        x, y = queue.popleft()

        for dx, dy in move_list:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and map_list[nx][ny] == '0':
                    visited[nx][ny] = True
                    area_map[nx][ny] = area_index
                    queue.append((nx, ny))
                    cnt += 1

    return cnt


# 빈칸 영역을 모두 BFS로 처리
for i in range(n):
    for j in range(m):
        if map_list[i][j] == '0' and not visited[i][j]:
            size = bfs(i, j)
            area_size_list.append(size)
            area_index += 1

# 최종 출력 지도
result_map = [[0] * m for _ in range(n)]

# 벽 기준으로 계산
for x in range(n):
    for y in range(m):
        if map_list[x][y] == '1':  # 벽인 경우 주변 영역 크기를 더해야 함
            area_set = set()
            total_cnt = 1  # 벽을 부쉈을 때 기본 이동 가능한 칸 1 포함

            for dx, dy in move_list:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    area_num = area_map[nx][ny]
                    if area_num != -1:
                        # 중복 방지를 위해 set 사용
                        if area_num not in area_set:
                            total_cnt += area_size_list[area_num]
                            area_set.add(area_num)

            result_map[x][y] = total_cnt % 10
        else:
            result_map[x][y] = 0

# 출력
for row in result_map:
    print("".join(map(str, row)))
