import sys

n = int(sys.stdin.readline().strip())
target_1, target_2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().strip())

graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
step = [-1] * (n + 1)

for i in range(m):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    graph[node_1][node_2] = graph[node_2][node_1] = True

bfs_queue = [target_1]
step[target_1] = 0
count = 0
while len(bfs_queue) != 0:
    next_step_count = 0
    node = bfs_queue.pop(0)

    for i in range(1, n + 1):
        if visited[i] == False and graph[node][i] == True:
            visited[i] = True
            step[i] = step[node] + 1
            bfs_queue.append(i)

print(step[target_2])