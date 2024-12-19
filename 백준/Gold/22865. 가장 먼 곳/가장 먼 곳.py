import sys
import heapq

n = int(sys.stdin.readline().strip())                       # 노드의 개수 저장
friend_list = list(map(int, sys.stdin.readline().strip().split()))    # 친구가 사는 위치 저장
m = int(sys.stdin.readline().strip())                       # 간선의 개수 저장

min_heap = []                                               # 최소 힙
INF = float('inf')
shortest_distance_list = [INF for _ in range(n + 1)]        # 최단 거리 테이블
n_list = [[] for _ in range(n + 1)]                         # 노드 사이 간선 정보

for _ in range(m):

    node1, node2, weight = map(int, sys.stdin.readline().strip().split())

    # 양방향 통행
    n_list[node1].append((node2, weight))
    n_list[node2].append((node1, weight))

for friend in friend_list:
    heapq.heappush(min_heap, (0, friend))

while min_heap:

    weight, node = heapq.heappop(min_heap)

    if weight <= shortest_distance_list[node]:

        shortest_distance_list[node] = weight

        for neighbor, neighbor_weight in n_list[node]:

            if neighbor_weight + weight <= shortest_distance_list[neighbor]:
                shortest_distance_list[neighbor] = neighbor_weight + weight
                heapq.heappush(min_heap, (neighbor_weight + weight, neighbor))

# print(shortest_distance_list)
max_distance = 0
max_i = 0
for i in range(1, n + 1):

    if shortest_distance_list[i] > max_distance:
        max_distance = shortest_distance_list[i]
        max_i = i

print(max_i)