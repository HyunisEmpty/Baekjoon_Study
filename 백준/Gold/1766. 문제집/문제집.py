import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
n_list = [[[], 0] for i in range(n + 1)]     # index 0: 진출 노드, index1 : 진입 노드 수
min_heap = []       # 최소 힙
visited = [False for i in range(n + 1)]

for _ in range(m):
    start_node, end_node = map(int, sys.stdin.readline().split())

    n_list[start_node][0].append(end_node)
    n_list[end_node][1] += 1

# print(n_list)

# 모든 노드에 대해 진입 노드가 없는 노드 탐색후 최소 힙에 저장
for i in range(1, len(n_list)):

    if n_list[i][1] == 0: # 진입 노드가 없는 경우
        heapq.heappush(min_heap, i)

# print(min_heap)

answer_list = []
while len(min_heap) > 0:

    local_root_node = heapq.heappop(min_heap)   # 진입 노드가 없는 노드
    visited[local_root_node] = True             # 방문 처리
    answer_list.append(local_root_node)

    for i in n_list[local_root_node][0]:    # 진출 노드 확인
        n_list[i][1] -= 1           # 진출 노드의 진입 노드 수 1 감소

        if n_list[i][1] == 0:    # 진출 노드가 더 이상 진입 노드가 없으며 방문하지 않은 경우
            heapq.heappush(min_heap, i)


print(*answer_list)