import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split())        # 도시, 도로, 면접장의 수
n_list = [[] for _ in range(n + 1)]                     # 간선 정보 저장 리스트
# INF = int(1e9)
INF = float('inf')
shortest_distance_list = [INF for _ in range(n + 1)]    # 최단 거리 테이블
min_heap = []                                           # 최소힙

for _ in range(m):      # 간선 정보 입력

    start, end, weight = map(int, sys.stdin.readline().split())
    n_list[end].append((start, weight))

k_list = list(map(int, sys.stdin.readline().split()))

for k_i in k_list:
    min_heap.append((0, k_i))

while min_heap:

    weight, node = heapq.heappop(min_heap)

    if weight < shortest_distance_list[node]:

        shortest_distance_list[node] = weight

        for neighbor, neighbor_weight in n_list[node]:

            if neighbor_weight + weight < shortest_distance_list[neighbor]:

                heapq.heappush(min_heap, (neighbor_weight + weight, neighbor))

# print(shortest_distance_list)
city_number = 0
max_distance = 0
for i in range(1, n + 1):

    if max_distance < shortest_distance_list[i] and shortest_distance_list[i] != INF:
        max_distance = shortest_distance_list[i]
        city_number = i

print(city_number)
print(max_distance)