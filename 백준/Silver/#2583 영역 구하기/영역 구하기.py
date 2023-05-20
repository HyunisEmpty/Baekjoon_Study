import sys

graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m, k = map(int, sys.stdin.readline().split())

# 그래프의 기본값을 설정하는 이중 for문
for i in range(n):
    graph.append([])
    for j in range(m):
        graph[i].append(1)

# 그래프의 직사각형의 구역에 해당하는 graph값을 1에서 0으로 바꾸는 for문
for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for delta_y in range(y2 - y1):
        for delta_x in range(x2 - x1):
            graph[y1 + delta_y][x1 + delta_x] = 0

def bfs(start_y, strat_x):
    deque = []
    deque.append((start_y, strat_x))
    cnt = 1

    while len(deque) != 0:
        y, x = deque.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > m - 1 or ny > n - 1 or ny < 0:
                continue
            else:
                if graph[ny][nx] == 1:
                    cnt += 1
                    graph[ny][nx] = 0
                    deque.append((ny, nx))

    return cnt

breadth = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            breadth.append(bfs(i, j))

breadth.sort()
print(len(breadth))
print(" ".join(map(str, breadth)))
