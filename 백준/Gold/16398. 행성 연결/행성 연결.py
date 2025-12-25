import sys
import heapq

node_cnt = int(sys.stdin.readline().strip())
node_list = []
node_set = set()
min_heap = []
answer = 0

for i in range(node_cnt):
    node_list.append(list(map(int, sys.stdin.readline().split())))

heapq.heappush(min_heap,(0 ,0))
while min_heap:
    weight, node = heapq.heappop(min_heap)

    if node not in node_set:
        answer += weight
        node_set.add(node)

        # 현재 노드와 연결된 모든 노드에 접근
        for next_node in range(node_cnt):
            if node_list[node][next_node] != 0 and next_node not in node_set:
                next_weight = node_list[node][next_node]
                heapq.heappush(min_heap, (next_weight, next_node))

print(answer)