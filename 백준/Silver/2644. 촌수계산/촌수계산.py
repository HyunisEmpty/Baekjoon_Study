import sys

n = int(sys.stdin.readline().strip())
target_1, target_2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().strip())

# 이중 리스트에서 현재 노드와 이와 접한 노드 번호를 인덱스로 하는 값을 접하는 경우 True 아닌경우 False로 한다.
graph = [[False] * (n + 1) for _ in range(n + 1)]
# 현재 노드가 이전에 접근했던 노드인지 확인하기 위한 리스트이다.
visited = [False] * (n + 1)
# 현재 노드가 루트 노드로 부터 몇번째 level에 있는지 확인하기 위함이며 루트노드와 연결되지 않는 경우 그 값이 -1이 된다.
step = [-1] * (n + 1)

# 두 노드 사이의 관계를 다음과 같이 정의 한다. 
for i in range(m):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    graph[node_1][node_2] = graph[node_2][node_1] = True

bfs_queue = [target_1]
step[target_1] = 0
while len(bfs_queue) != 0:
    next_step_count = 0
    node = bfs_queue.pop(0)

    for i in range(1, n + 1):
        # 방문한적 없으며 현재 노드와 접하는 경우
        if visited[i] == False and graph[node][i] == True:
            visited[i] = True
            step[i] = step[node] + 1
            bfs_queue.append(i)

print(step[target_2])