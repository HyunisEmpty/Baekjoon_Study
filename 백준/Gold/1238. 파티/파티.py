import sys
import heapq
INF = int(1e9)


# 다익스트라 알고리즘 (시작섬, 최단 거리 테이블, 인접 노드 리스트)
def Dijkstra(start, shortest_distance_list, neighbor_list):

    global min_queue
    global visited

    min_queue.clear()
    visited.clear()

    heapq.heappush(min_queue, (0, start))
    back_shortest_distance_list[start] = 0

    # 시작 섬에서 각자 섬으로 갈때 다익스트라 알고리즘
    while min_queue:

        weight, node = heapq.heappop(min_queue)

        if node not in visited:  # 방문 여부 판단
            visited.add(node)
            shortest_distance_list[node] = weight

            for neighbor, neighbor_weight in neighbor_list[node]:  # 인접 노드 접근

                if neighbor not in visited:
                    heapq.heappush(min_queue, (neighbor_weight + weight, neighbor))


n, m, x = map(int, sys.stdin.readline().split())
back_list = [[] for _ in range(n + 1)]          # 파티 -> 집 인접 마을 리스트
go_list = [[] for _ in range(n + 1)]            # # 집 -> 파티 인접 마을 리스트
back_shortest_distance_list = [INF for _ in range(n + 1)]       # 파티 -> 집 최단 경로 테이블
go_shortest_distance_list = [INF for _ in range(n + 1)]         # 집 -> 파티 최단 경로 테이블

min_queue = []
visited = set()

for _ in range(m):  # 간선 정보 입력
    start, end, weight = map(int, sys.stdin.readline().split())
    back_list[start].append((end, weight))
    go_list[end].append((start, weight))

Dijkstra(x, back_shortest_distance_list, back_list)
Dijkstra(x, go_shortest_distance_list, go_list)

answer = 0
for i in range(1, n + 1):
    answer = max(answer, go_shortest_distance_list[i] + back_shortest_distance_list[i])

print(answer)

