import sys

N, M = map(int, sys.stdin.readline().split())

# 2차원 리스트
graph = [[False for _ in range(N + 1)] for _ in range(N + 1)]

# 자기 자신에게 가는 비용은 0으로 초기화
for node1 in range(1, N + 1):
    for node2 in range(1, N + 1):
        if node1 == node2:
            graph[node1][node2] = True

# 간선 정보 저장
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().strip().split())
    graph[node1][node2] = True

# 플로이드 워셜 알고리즘 수행
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if graph[a][k] and graph[k][b]:     # a -> k -> b 경로가 존재하면
                graph[a][b] = True      # a -> b 경로가 존재

# 수행된 결과를 출력
cnt_list = [0 for _ in range(N + 1)]
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if graph[a][b] or graph[b][a]:  # i -> j 또는 j -> i 경로가 존재하면
            cnt_list[a] += 1

answer = 0
for count in cnt_list:
    if count == N:
        answer += 1

print(answer)

