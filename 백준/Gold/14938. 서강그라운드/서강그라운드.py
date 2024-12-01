import sys
import heapq

n, m, r = map(int, sys.stdin.readline().split())    # n: 지역의 개수, m: 수색범위, r: 길의 개수
t_list = list(map(int, sys.stdin.readline().split()))   # 각 지역별 아이템의 수

n_list = [[] for _ in range(n + 1)]
for _ in range(r):
    start, end, weight = map(int, sys.stdin.readline().split())

    # 양 방향 통행이 가능하다.
    n_list[start].append((end, weight))
    n_list[end].append((start, weight))

max_item = 0

# 모든 지역을 한번씩 낙하 지점으로 선정
for drop_point in range(1, n + 1):

    now_item = 0  # 현재의 낙하지점을 통해 수집한 아이템의 수
    visited = [False for _ in range(n + 1)] # 방문 여부 저장

    min_heap = [(0, drop_point)]    # 최소힙 (간선 가중치합, 현재 노드)

    while min_heap:

        now_weight, now_drop_point = heapq.heappop(min_heap)

        if not visited[now_drop_point]:     # 방문 한 적 없는 경우
            now_item += t_list[now_drop_point-1]
            visited[now_drop_point] = True

            for neighbor, neighbor_weight in n_list[now_drop_point]:
                if neighbor_weight + now_weight <= m:   # 수색 범위 안에 있는 경우
                    heapq.heappush(min_heap, (neighbor_weight + now_weight, neighbor))

    max_item = max(now_item, max_item)

print(max_item)