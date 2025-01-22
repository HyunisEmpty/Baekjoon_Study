import sys

N, M = map(int, sys.stdin.readline().split())

# 2차원 리스트
graph = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]

# 자기 자신에게 가는 비용은 0으로 초기화
for node1 in range(1, N + 1):
    for node2 in range(1, N + 1):
        if node1 == node2:
            graph[node1][node2] = 0

# 간선 정보 저장
for _ in range(M):
    node1, node2, weight = map(int, sys.stdin.readline().strip().split())
    graph[node1][node2] = min(weight, graph[node1][node2])

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# # 수행된 결과를 출력
# for a in range(1, N + 1):
#     for b in range(1, N + 1):
#         if graph[a][b] == float('inf'):
#             print('0', end=' ')
#         else:
#             print(graph[a][b], end=' ')
#     print()

answer = -1
for a in range(1, N + 1):
    for b in range(1, N + 1):
        # 사이클이 있는 경우
        if a != b:
            if graph[a][b] != float('inf') and graph[b][a] != float('inf'):

                if answer == -1:
                    answer = graph[a][b] + graph[b][a]
                else:
                    answer = min(graph[a][b] + graph[b][a], answer)

print(answer)