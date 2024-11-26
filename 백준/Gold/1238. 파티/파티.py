import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())

INF = int(1e9)
back_list = [[] for _ in range(n + 1)]
go_list = [[] for _ in range(n + 1)]
shortest_distance_list = [INF for _ in range(n + 1)]
min_queue = []
visited = set()

for _ in range(m):  # 간선 정보 입력
    start, end, weight = map(int, sys.stdin.readline().split())
    back_list[start].append((end, weight))
    go_list[end].append((start, weight))

heapq.heappush(min_queue, (0, x))
shortest_distance_list[x] = 0

# 시작 섬에서 각자 섬으로 갈때 다익스트라 알고리즘
while min_queue:

    weight, node = heapq.heappop(min_queue)

    if node not in visited:  # 방문 여부 판단
        visited.add(node)
        shortest_distance_list[node] = weight

        for end, end_weight in back_list[node]:    # 인접 노드 접근

            if end not in visited:
                heapq.heappush(min_queue, (end_weight + weight, end))

shortest_distance_list2 = [INF for _ in range(n + 1)]
min_queue = []
heapq.heappush(min_queue, (0, x))
shortest_distance_list2[x] = 0
visited = set()

# 각자 섬에서 시작 섬으로 올 때 다익스트라 알고리즘
while min_queue:

    weight, node = heapq.heappop(min_queue)

    if node not in visited:  # 방문 여부 판단
        visited.add(node)
        shortest_distance_list2[node] = weight

        for end, end_weight in go_list[node]:    # 인접 노드 접근

            if end not in visited:
                heapq.heappush(min_queue, (end_weight + weight, end))

answer = 0
for i in range(1, n + 1):

    answer = max(answer, shortest_distance_list2[i] + shortest_distance_list[i])

print(answer)

