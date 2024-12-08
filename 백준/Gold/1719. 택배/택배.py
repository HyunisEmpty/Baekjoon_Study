import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

n_list = [[] for _ in range(n + 1)]         # 노드 별 인접 노드를 저장하는 리스트
min_heap = []                               # 최소 힙

for _ in range(m):      # 간선 정보 저장

    node1, node2, weight = map(int, sys.stdin.readline().split())

    # 양방향
    n_list[node1].append((node2, weight))
    n_list[node2].append((node1, weight))


# 최단 경로로 화물을 이동시키기 위해 가장 먼저 거쳐야 하는 집하장
def FindFirstNode(before_node, now_node, first_n_list):

    if now_node == before_node:     # 시작 노드인 경우
        first_n_list[now_node] = "-"
    else:
        if first_n_list[before_node] == "-":    # 이전 노드가 시작 노드인 경우
            first_n_list[now_node] = str(now_node)
        else:                                   # 이전 노드가 시작 노드가 아닌 경우
            first_n_list[now_node] = first_n_list[before_node]


# 다익스트라 알고리즘 정의
def Dijkstra(first_node):

    first_n_list = [0 for _ in range(n + 1)]  # 가장 먼저 거쳐야 하는 집하장 저장 리스트
    min_heap.clear()                                    # 최소힙 초기화
    visited = [False] * (n + 1)                         # 노드 방문 여부 저장 리스트
    shortest_distance_list = [0 for _ in range(n + 1)]  # 최단 거리 테이블

    shortest_distance_list[first_node] = 0
    first_n_list[first_node] = "-"
    before_node = first_node
    heapq.heappush(min_heap, (shortest_distance_list[first_node], first_node, before_node))
    while min_heap:

        weight, node, before_node = heapq.heappop(min_heap)

        if not visited[node]:   # 방문하지 않은 경우

            visited[node] = True                    # 현재 노드 방문 여부 확인
            shortest_distance_list[node] = weight   # 현재 노드 최단 거리 테이블 업데이트
            FindFirstNode(before_node, node, first_n_list)         # 가장 먼저 거쳐야 하는 집하장 저장

            for neighbor, neighbor_weight in n_list[node]:  # 이웃 노드 접근

                if not visited[neighbor]:                       # 아직 접근(최단 거리가 결정) 하지 않았다면
                    heapq.heappush(min_heap, (neighbor_weight + weight, neighbor, node))

    print(" ".join(map(str, first_n_list[1:])))

# 1번 노드부터 N번 노드 까지 접근
for first_node in range(1, n + 1):
    Dijkstra(first_node)