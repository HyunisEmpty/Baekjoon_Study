import sys
from collections import deque

cnt = 1
while True:

    n = int(sys.stdin.readline().strip())

    if n == 0:
        break

    n_list = []
    for _ in range(n):
        n_list.append(list(map(int, sys.stdin.readline().strip().split())))

    min_n_list = [[0 for _ in range(n)] for _ in range(n)]      # 각 노드로 도착하는데 드는 최소 루피
    visited = [[False for _ in range(n)] for _ in range(n)]

    queue = deque()
    queue.append((0, 0))
    min_n_list[0][0] = n_list[0][0]
    visited[0][0] = True
    while queue:

        x, y = queue.popleft()

        for nx, ny in [[-1, 0], [1, 0], [0, -1], [0, 1]]:       # 상하좌우 접근
            dx, dy = x + nx, y + ny
            if 0 <= dx < n and 0 <= dy < n:

                if not visited[dx][dy] or min_n_list[x][y] + n_list[dx][dy] < min_n_list[dx][dy]:
                    min_n_list[dx][dy] = min_n_list[x][y] + n_list[dx][dy]
                    visited[dx][dy] = True
                    queue.append((dx, dy))

    print("Problem {}: {}".format(cnt, min_n_list[n-1][n-1]))

    cnt += 1