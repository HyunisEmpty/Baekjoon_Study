import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

n_list = [[] for _ in range(n + 1)]                     # 간선 정보 저장
INF = float('inf')
min_heap = []                                           # 최소 힙

for _ in range(m):

    start, end, weight = map(int, sys.stdin.readline().split())

    n_list[start].append((end, weight))

x, y, z = map(int, sys.stdin.readline().split())

def Dijkstra(start, cant_access):

    shortest_distance_list = [INF for _ in range(n + 1)]  # 최단 거리 테이블

    shortest_distance_list[start] = 0
    heapq.heappush(min_heap, (shortest_distance_list[start], start))

    while min_heap:

        weight, node = heapq.heappop(min_heap)

        if weight <= shortest_distance_list[node]:

            shortest_distance_list[node] = weight

            for neighbor, neighbor_weight in n_list[node]:

                if neighbor != cant_access and neighbor_weight + weight <= shortest_distance_list[neighbor]:
                    shortest_distance_list[neighbor] = weight + neighbor_weight
                    heapq.heappush(min_heap, (shortest_distance_list[neighbor], neighbor))

    return shortest_distance_list

xyz_sdl = Dijkstra(x,0)
yz_sdl = Dijkstra(y,0)
xz_sdl = Dijkstra(x, y)

xyz = xyz_sdl[y] + yz_sdl[z]
xz = xz_sdl[z]

if xz == INF:
    xz = -1

if xyz == INF:
    xyz = -1


print(xyz, xz)