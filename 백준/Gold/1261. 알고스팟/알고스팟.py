import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
queue = deque()

map_list = []
for _ in range(n):
    map_list.append(sys.stdin.readline().strip())   # 지도 정보

wall_cnt_list = [[0 for _ in range(m)] for _ in range(n)]   # 노드까지 오기 위해 몇번의 벽을 부섰는지
visited = [[False for _ in range(m)] for _ in range(n)]     # 방문 여부

queue.append((0, 0, 0)) # x, y, 벽을 부순 개수 저장

while queue:

    x, y, wall_cnt = queue.popleft()

    # 상하좌우 접근
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:         # 미로 내에 있는지

            if not visited[nx][ny]:     # 첫 방문인경우

                visited[nx][ny] = True      # 방문 했다고 체크
                if map_list[nx][ny] == '1':     # 벽인 경우
                    queue.append((nx, ny, wall_cnt + 1))
                    wall_cnt_list[nx][ny] = wall_cnt + 1
                else:                           # 빈방인 경우
                    queue.append((nx, ny, wall_cnt))
                    wall_cnt_list[nx][ny] = wall_cnt

            else:                       # 첫 방문이 아닌 경우
                if map_list[nx][ny] == '1' and wall_cnt + 1 < wall_cnt_list[nx][ny]:  # 벽인 경우
                    queue.append((nx, ny, wall_cnt + 1))
                    wall_cnt_list[nx][ny] = wall_cnt + 1
                elif map_list[nx][ny] == '0' and wall_cnt < wall_cnt_list[nx][ny]:                        # 빈방인 경우
                    queue.append((nx, ny, wall_cnt))
                    wall_cnt_list[nx][ny] = wall_cnt

print(wall_cnt_list[n-1][m-1])