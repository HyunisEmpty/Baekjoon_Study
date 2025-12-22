import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

n_list = [[] for _ in range(N + 1)]
node_set = set()
max_weight = 0
total_weight = 0
min_heap = []


for _ in range(M):
    node1, node2, weight = map(int, sys.stdin.readline().split())

    n_list[node1].append((node2, weight))
    n_list[node2].append((node1, weight))

# 프림 알고리즘의 시작 노드는 1로 한다.
heapq.heappush(min_heap, (0, 1))
while min_heap:
    weight, node = heapq.heappop(min_heap)

    if node not in node_set:
        node_set.add(node)
        total_weight += weight

        if max_weight < weight:
            max_weight = weight

        for next_node, next_weight in n_list[node]:
            if next_node not in node_set:
                heapq.heappush(min_heap, (next_weight, next_node))

print(total_weight - max_weight)
