import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

# BFS 알고리즘
while queue:

    x, y = queue.popleft()

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
            matrix[nx][ny] = matrix[x][y] + 1
            queue.append([nx, ny])

for i in matrix:
    if 0 in i:
        res = 0
        break
    res = max(res, max(i))

# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res - 1)