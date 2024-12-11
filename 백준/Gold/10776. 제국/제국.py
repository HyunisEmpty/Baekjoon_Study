import sys
import heapq

k, n, m = map(int, sys.stdin.readline().split())
n_list = [[] for _ in range(n + 1)]                     # 노드 사이의 간선의 관계 저장
INF = int(1e9)
shortest_distance_list = [INF for _ in range(n + 1)]      # 최단 거리 테이블
min_hi_list = [INF for _ in range(n + 1)]                      # 뗏목의 길이를 저장하는 리스트
min_heap = []                                           # 최소 힙

for _ in range(m):

    a, b, t, h = map(int, sys.stdin.readline().split())

    # 바닷길은 양방향인 것 같다.
    n_list[a].append((b, t, h))
    n_list[b].append((a, t, h))

start_node, end_node = map(int, sys.stdin.readline().split())

shortest_distance_list[start_node] = 0      # 최단 거리 테이블
min_hi_list[start_node] = 0                 # 현재 까지 잘린 뗏목의 길이 저장 리스트
heapq.heappush(min_heap, (0, 0, start_node))
while min_heap:

    weight, hi, node = heapq.heappop(min_heap)

    # 현재 노드에 접근할때, 최단거리가 아니거나 뗏목의 길이가 더 짧은 경우는 제외
    if weight <= shortest_distance_list[node] or hi < min_hi_list[node]:

        shortest_distance_list[node] = weight
        min_hi_list[node] = hi

        if node == end_node and hi < k:    # 종료 조건
            break

        for neighbor, neighbor_weight, neighbor_hi in n_list[node]:

            if neighbor_weight + weight <= shortest_distance_list[neighbor] or hi + neighbor_hi < min_hi_list[neighbor]:

                heapq.heappush(min_heap, (neighbor_weight + weight, hi + neighbor_hi,neighbor))

if min_hi_list[end_node] >= k:
    print(-1)
else:
    print(shortest_distance_list[end_node])
