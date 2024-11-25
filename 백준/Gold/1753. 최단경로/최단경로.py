import sys
import heapq
from collections import deque

v, e = map(int, sys.stdin.readline().split())       # v: 노드 개수, e: 간선 개수
start_v = int(sys.stdin.readline().strip())         # 시작 노드
v_list = [[] for _ in range(v + 1)]                 # 노드 사이의 연결 정보 저장
INF = int(1e9)
shortest_distance_list = [INF for _ in range(v + 1)]         # 시작 노드로 부터 최단 거리 저장
min_heap = []
visited = set()     # 방문 노드 저장


# 간선 정보 입력
for _ in range(e):

    # node1에서 node2로 가는 간선 가중치는 weight
    node1, node2, weight = map(int, sys.stdin.readline().split())

    v_list[node1].append((weight, node2))

heapq.heappush(min_heap, (0, start_v))

while min_heap:

    weight, node = heapq.heappop(min_heap)

    if node not in visited:     # 방문 한적 없는 경우
        visited.add(node)

        # 주변 노드 접근
        for info in v_list[node]:
            neighbor_weight, neighbor = info
            heapq.heappush(min_heap, (weight + neighbor_weight, neighbor))

        shortest_distance_list[node] = weight

for i in range(1, len(shortest_distance_list)):
    if shortest_distance_list[i] == INF:
        print("INF")
    else:
        print(shortest_distance_list[i])
