import sys
import heapq

n, e = map(int, sys.stdin.readline().split())   # n : 노드 수, e : 간선 수
n_list = [[] for _ in range(n + 1)]                 # 노드 사이 간선 정보 입력
INF = int(1e9)

for _ in range(e):
    n1, n2, c = map(int, sys.stdin.readline().split())

    # 무방향 그래프
    n_list[n1].append((n2, c))
    n_list[n2].append((n1, c))

v1, v2 = map(int, sys.stdin.readline().split())


def Dijkstra(start, end):

    global n_list       # n_list

    visited = set()     # 방문 여부
    min_heap = []       # 최소 힙
    shortest_distance_list = [INF for _ in range(n + 1)]

    heapq.heappush(min_heap, (0, start))

    while min_heap:

        weight, node = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)

            for info in n_list[node]:   # 주변 노드 접근
                neighbor_node, neighbor_weight = info
                heapq.heappush(min_heap, (neighbor_weight + weight, neighbor_node))

            shortest_distance_list[node] = weight

        if end in visited:
            break

    return shortest_distance_list[end]


startToV1 = Dijkstra(1, v1)
startToV2 = Dijkstra(1, v2)
v1ToV2 = Dijkstra(v1, v2)
v1ToEnd = Dijkstra(v1, n)
v2ToEnd = Dijkstra(v2, n)

path1 = startToV1 + v1ToV2 + v2ToEnd
path2 = startToV2 + v1ToV2 + v1ToEnd

if path1 > INF or path2 > INF:
    print(-1)
else:
    print(min(path1, path2))