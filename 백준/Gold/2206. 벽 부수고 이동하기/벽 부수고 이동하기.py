import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
n_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

queue1 = deque()
queue2 = deque()
wall_set = set()

# 1번 BFS 알고리즘
queue1.append((0, 0))
wall_set.add((0, 0))
n_list[0][0] = 1
while queue1:

    x, y = queue1.popleft()

    for nx, ny in [(1, 0), (-1, 0), (0, 1), (0, -1)]:   # 상하좌우 접근
        dx, dy = x + nx, y + ny
        if 0 <= dx < n and 0 <= dy < m: # 상하좌우 땅이 인덱스 범위 내에 있는지

            # 벽이 아니면서 최단 거리 최신화가 가능한 경우
            if n_list[dx][dy] == 0 or n_list[x][y] + 1 < n_list[dx][dy]:
                n_list[dx][dy] = n_list[x][y] + 1
                queue1.append((dx, dy))

            # 벽인 경우
            if n_list[dx][dy] == 1 and (dx, dy) not in wall_set:
                queue2.append((dx, dy, n_list[x][y] + 1)) # 벽의 좌표 벽에 들어간 최솟값 저장
                wall_set.add((dx, dy))

# 2번 BFS 알고리즘
while queue2:

    x, y, time = queue2.popleft()

    for nx, ny in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dx, dy = x + nx, y + ny
        if 0 <= dx < n and 0 <= dy < m:

            # 벽이 아니면서 최단 거리 최신화가 가능한 경우
            if n_list[dx][dy] == 0 or time + 1 < n_list[dx][dy]:
                n_list[dx][dy] = time + 1
                queue2.append((dx, dy, time + 1))

# for i in range(n):
#     print(n_list[i])

if n_list[n-1][m-1] == 0:
    print(-1)
else:
    print(n_list[n-1][m-1])