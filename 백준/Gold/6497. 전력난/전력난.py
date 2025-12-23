import sys
import heapq

while True:
    node_cnt, vertex_cnt = map(int, sys.stdin.readline().split())
    node_list = [[] for _ in range(node_cnt)]
    node_set = set()
    min_heap = []
    total_weight = 0
    min_weight = 0

    if node_cnt == 0 and vertex_cnt == 0:
        break

    for i in range(vertex_cnt):
        node1, node2, weight = map(int, sys.stdin.readline().split())
        total_weight += weight

        node_list[node1].append((node2, weight))
        node_list[node2].append((node1, weight))

    min_heap.append((0, 0))
    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node not in node_set:
            node_set.add(node)
            min_weight += weight

            for neighbor_node, neighbor_weight in node_list[node]:
                if neighbor_node not in node_set:
                    heapq.heappush(min_heap, (neighbor_weight, neighbor_node))

    print(total_weight - min_weight)
