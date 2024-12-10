import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

INF = int(1e9)
shortest_distance_list = [INF for _ in range(n + 1)]    # 최단 거리 테이블
visited = [False for _ in range(n + 1)]                 # 노드별 방문 여부 저장
min_heap = []                                           # 최소 힙
shortest_distance_edge_list = []

n_list = [[] for _ in range(n + 1)]
for _ in range(m):      # 간선 정보 저장

    node1, node2, weight = map(int, sys.stdin.readline().split())

    n_list[node1].append((node2, weight))
    n_list[node2].append((node1, weight))

shortest_distance_list[1] = 0   # 1번 컴퓨터는 보안 시스템을 설치할 슈퍼컴퓨터이다.
heapq.heappush(min_heap, (shortest_distance_list[1], 1, 1))
while min_heap:

    weight, node, before_node = heapq.heappop(min_heap)

    if not visited[node]:

        visited[node] = True
        shortest_distance_list[node] = weight

        if node != before_node:
            shortest_distance_edge_list.append(str(node) + " " + str(before_node))

        for neighbor, neighbor_weight in n_list[node]:

            if not visited[neighbor]:
                heapq.heappush(min_heap, (neighbor_weight + weight, neighbor, node))

print(len(shortest_distance_edge_list))
for i in range(len(shortest_distance_edge_list)):
    print(shortest_distance_edge_list[i])