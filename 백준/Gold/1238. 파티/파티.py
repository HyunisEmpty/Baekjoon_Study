import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())

INF = int(1e9)
back_list = [[] for _ in range(n + 1)]
go_list = [[] for _ in range(n + 1)]
back_shortest_distance_list = [INF for _ in range(n + 1)]
go_shortest_distance_list = [INF for _ in range(n + 1)]
min_queue = []
visited = set()

for _ in range(m):  # 간선 정보 입력
    start, end, weight = map(int, sys.stdin.readline().split())
    back_list[start].append((end, weight))
    go_list[end].append((start, weight))

heapq.heappush(min_queue, (0, x))
back_shortest_distance_list[x] = 0

# 시작 섬에서 각자 섬으로 갈때 다익스트라 알고리즘
while min_queue:

    weight, node = heapq.heappop(min_queue)

    if node not in visited:  # 방문 여부 판단
        visited.add(node)
        back_shortest_distance_list[node] = weight

        for end, end_weight in back_list[node]:    # 인접 노드 접근

            if end not in visited:
                heapq.heappush(min_queue, (end_weight + weight, end))

min_queue.clear()       # 최소힙 초기화 
visited.clear()         # 집합 초기화 
heapq.heappush(min_queue, (0, x))
go_shortest_distance_list[x] = 0

# 각자 섬에서 시작 섬으로 올 때 다익스트라 알고리즘
while min_queue:

    weight, node = heapq.heappop(min_queue)

    if node not in visited:  # 방문 여부 판단
        visited.add(node)
        go_shortest_distance_list[node] = weight

        for end, end_weight in go_list[node]:    # 인접 노드 접근

            if end not in visited:
                heapq.heappush(min_queue, (end_weight + weight, end))

answer = 0
for i in range(1, n + 1):

    answer = max(answer, go_shortest_distance_list[i] + back_shortest_distance_list[i])

print(answer)

