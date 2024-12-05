import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split())    # n : 노드, m : 간선, k : k번째 최단경로

n_list = [[] for _ in range(n + 1)]
for _ in range(m):      # 간선 정보 입력
    a, b, c = map(int, sys.stdin.readline().split())
    n_list[a].append((b, c))

INF = int(1e9)
shortest_distance_list = [INF for _ in range(n + 1)]    # 최단 거리 테이블
shortest_distance_update_list = [0 for _ in range(n + 1)]
min_heap = []

shortest_distance_list[1] = 0   # 시작 노드
heapq.heappush(min_heap, (shortest_distance_list[1], 1))

while min_heap:

    weight, node = heapq.heappop(min_heap)

    if shortest_distance_update_list[node] != k:   # 방문 하지 않은 경우
        shortest_distance_list[node] = weight
        shortest_distance_update_list[node] += 1

        for neighbor, neighbor_weight in n_list[node]:

            if shortest_distance_update_list[neighbor] != k:
                heapq.heappush(min_heap, (weight + neighbor_weight, neighbor))

for node in range(1, n + 1):

    if shortest_distance_update_list[node] == k:    # k번째 경로가 존재 하는 경우
        print(shortest_distance_list[node])
    else:
        print(-1)
