import sys
import heapq

n, m = map(int, sys.stdin.readline().split())               # 노드와 간선의 개수 저장

INF = float('inf')
n_list = [[] for _ in range(n + 1)]                         # 간선 사이 가중치 정보 저장
min_heap = []                                               # 최소 힙

for _ in range(m):      # 간선 사이의 정보 입력

    node1, node2, weight = map(int, sys.stdin.readline().split())

    n_list[node1].append((node2, weight))
    n_list[node2].append((node1, weight))

MCD, x = map(int, sys.stdin.readline().split())             # 맥도날드 매장수와, x
MCD_list = list(map(int, sys.stdin.readline().split()))     # 맥도날드 매장의 위치

SBUX, y = map(int, sys.stdin.readline().split())            # 스타벅스 매장수와, y
SBUX_list = list(map(int, sys.stdin.readline().split()))    # 스탑벅스 매장의 위치

store_set = set(MCD_list) | set(SBUX_list)                  # 집이 될 수 없는 위치

def Dijkstra(store_list, distance_limit):

    shortest_distance_list = [INF for _ in range(n + 1)]  # 최단 거리 테이블
    house_set = set()

    # 최소 힙 초기화
    for store in store_list:

        shortest_distance_list[store] = 0
        heapq.heappush(min_heap, (shortest_distance_list[store], store))

    while min_heap:

        weight, node = heapq.heappop(min_heap)

        if weight <= shortest_distance_list[node]:

            shortest_distance_list[node] = weight

            for neighbor, neighbor_weight in n_list[node]:

                if neighbor_weight + weight <= shortest_distance_list[neighbor]:
                    shortest_distance_list[neighbor] = neighbor_weight + weight
                    heapq.heappush(min_heap, (shortest_distance_list[neighbor], neighbor))

    for i in range(1, n + 1):

        if shortest_distance_list[i] <= distance_limit and (i not in store_set):
            house_set.add(i)

    return house_set, shortest_distance_list

MCD_set, MCD_sdl = Dijkstra(MCD_list, x)
SBUX_set, SBUX_sdl = Dijkstra(SBUX_list, y)
MCD_SBUX_set = MCD_set & SBUX_set

# print(store_set)
#
# print(MCD_sdl)
# print(SBUX_sdl)
#
# print(MCD_set)
# print(SBUX_set)


if len(MCD_SBUX_set) == 0:
    print(-1)
else:
    min_distance = INF
    for MCD_SBUX in MCD_SBUX_set:

        # print(MCD_SBUX, MCD_sdl[MCD_SBUX] + SBUX_sdl[MCD_SBUX])
        min_distance = min(min_distance, MCD_sdl[MCD_SBUX] + SBUX_sdl[MCD_SBUX])

    print(min_distance)