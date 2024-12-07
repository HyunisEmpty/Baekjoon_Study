import sys
import heapq

# n : 노드, m : 간선
n, m = map(int, sys.stdin.readline().split())

INF = int(1e9)
shortest_distance_list = [INF] * (n)    # 최단 거리 테이블
visited = [False] * (n)                 # 방문 여부 저장
min_heap = []                           # 최소 힙

vision_list = list(map(int, sys.stdin.readline().split()))   # 시야에 보이는지 여부
for i in range(1, n):
    vision = vision_list[i]     # 시야 정보
    if vision and i != n - 1:  # vision이 1이면서 넥서스가 아닌 경우
        visited[i] = True

n_list = [[] for _ in range(n)] # 간선 정보 입력
for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())

    # 양 방향
    n_list[start].append((end, weight))
    n_list[end].append((start, weight))

shortest_distance_list[0] = 0
heapq.heappush(min_heap, (shortest_distance_list[0], 0))
while min_heap:

    weight, node = heapq.heappop(min_heap)

    if not visited[node]:       # 방문하지 않은 경우

        visited[node] = True
        shortest_distance_list[node] = weight

        for neighbor, neighbor_weight in n_list[node]:

            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight + neighbor_weight, neighbor))

if shortest_distance_list[n-1] == INF:
    print(-1)
else:
    print(shortest_distance_list[n-1])