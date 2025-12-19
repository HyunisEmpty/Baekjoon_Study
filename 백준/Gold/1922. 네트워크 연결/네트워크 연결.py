import sys
import heapq

N = int(sys.stdin.readline().strip())   # 컴퓨터(정점)의 수
M = int(sys.stdin.readline().strip())   # 선(간선)의 수
node_list = [[] for i in range(N + 1)]
node_set = set()
min_heap = [(0, 1)]
answer = 0

for _ in range(M):
    node1, node2, weight = map(int, sys.stdin.readline().split())

    if(node1 == node2):
        continue

    node_list[node1].append((node2, weight))
    node_list[node2].append((node1, weight))

while min_heap:
    weight, node = heapq.heappop(min_heap)

    if node not in node_set:
        node_set.add(node)
        answer += weight

        for next_node, next_weight in node_list[node]:
            if next_node not in node_set:
                heapq.heappush(min_heap, (next_weight, next_node))

print(answer)