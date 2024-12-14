import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
n_list = [[] for _ in range(n + 1)]
min_heap = []
INF = int(1e9)
shortest_distance_list = [INF for _ in range(n + 1)]

for _ in range(m):

    node1, node2, weight = map(int, sys.stdin.readline().split())

    n_list[node1].append((node2, weight))
    n_list[node2].append((node1, weight))

start_node, end_node = map(int, sys.stdin.readline().split())

shortest_distance_list[start_node] = 0
heapq.heappush(min_heap, (0, start_node))
while min_heap:

    weight, node = heapq.heappop(min_heap)

    if weight <= shortest_distance_list[node]:

        shortest_distance_list[node] = weight

        for neighbor, neighbor_weight in n_list[node]:

            if neighbor_weight + weight <= shortest_distance_list[neighbor]:
                shortest_distance_list[neighbor] = weight + neighbor_weight
                heapq.heappush(min_heap, (weight + neighbor_weight, neighbor))

print(shortest_distance_list[end_node])