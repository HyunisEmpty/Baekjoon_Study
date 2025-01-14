import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

INF = float('inf')
map_list = [list(sys.stdin.readline().strip()) for _ in range(n)]   # 지도 정보 저장
shortest_distance_list = [[INF for _ in range(m + 1)] for _ in range(n + 1)]    # 최단거리 테이블 생성
visited = [[False for _ in range(m + 1)] for _ in range(n + 1)]
min_heap = []

# 간선 생성
e_list = [[[] for _ in range(m + 1)] for _ in range(n + 1)]      # 간선(Edge)의 정보 저장
for x in range(n):
    for y in range(m):

        if map_list[x][y] == '\\':

            # 가중치가 0인 간선
            e_list[x][y].append(((x + 1, y + 1), 0))
            e_list[x + 1][y + 1].append(((x, y), 0))

            # 가중치가 1인 간선
            e_list[x + 1][y].append(((x, y + 1), 1))
            e_list[x][y + 1].append(((x + 1, y), 1))

        elif map_list[x][y] == '/':

            # 가중치가 1인 간선
            e_list[x][y].append(((x + 1, y + 1), 1))
            e_list[x + 1][y + 1].append(((x, y), 1))

            # 가중치가 1인 간선
            e_list[x + 1][y].append(((x, y + 1), 0))
            e_list[x][y + 1].append(((x + 1, y), 0))

shortest_distance_list[0][0] = 0
heapq.heappush(min_heap, (0, (0, 0)))
visited[0][0] = True
while min_heap:

    weight, node_position = heapq.heappop(min_heap)
    x, y = node_position

    if weight <= shortest_distance_list[x][y]:  # 최단 거리로 접근 하는 경우
        shortest_distance_list[x][y] = weight

        for neighbor_position, neighbor_weight in e_list[x][y]:
            nx, ny = neighbor_position
            if not visited[nx][ny]:     # 방문한 적 없는 경우
                shortest_distance_list[nx][ny] = neighbor_weight + weight
                heapq.heappush(min_heap, (weight + neighbor_weight, (nx, ny)))
                visited[nx][ny] = True
            else:                       # 방문한 적 있는 경우
                if neighbor_weight + weight < shortest_distance_list[nx][ny]:
                    shortest_distance_list[nx][ny] = neighbor_weight + weight
                    heapq.heappush(min_heap, (weight + neighbor_weight, (nx, ny)))

if shortest_distance_list[n][m] == INF:
    print("NO SOLUTION")
else:
    print(shortest_distance_list[n][m])