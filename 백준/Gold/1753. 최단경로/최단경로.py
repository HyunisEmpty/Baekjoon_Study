import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
x = int(sys.stdin.readline().strip())

INF = int(1e9)
n_list = [[] for _ in range(n + 1)]
shortest_distance_list = [INF for _ in range(n + 1)]
min_queue = []
visited = set()

for _ in range(m):  # 간선 정보 입력
    start, end, weight = map(int, sys.stdin.readline().split())
    n_list[start].append((end, weight))

heapq.heappush(min_queue, (0, x))
shortest_distance_list[x] = 0

while min_queue:

    weight, node = heapq.heappop(min_queue)

    if node not in visited:  # 방문 여부 판단
        visited.add(node)
        shortest_distance_list[node] = weight

        for end, end_weight in n_list[node]:    # 인접 노드 접근

            if end not in visited:
                heapq.heappush(min_queue, (end_weight + weight, end))

for i in range(1, len(shortest_distance_list)):
    if shortest_distance_list[i] == INF:
        print("INF")
    else:
        print(shortest_distance_list[i])


