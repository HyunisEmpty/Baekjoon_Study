import sys
import heapq

N, M, D, E = map(int, sys.stdin.readline().split())             # 지점의 개수, 경로의 개수, 거리 비례 체력 소모량, 높이 비례 성취감 회득량
h_list = [0] + list(map(int, sys.stdin.readline().split()))     # 각 지점의 높이 저장
INF = float('inf')

# 노드사이의 연결 관계 저장
m_list = [[] for _ in range(N + 1)]
for _ in range(M):

    node1, node2, weight = map(int, sys.stdin.readline().split())

    # 양방향 간선
    m_list[node1].append((node2, weight))
    m_list[node2].append((node1, weight))


def Dijkstra(start):

    min_heap = []       # 최소힙
    shortest_distance_list = [INF for _ in range(N + 1)]      # 최단 거리 테이블

    # 출발 지점 초기값 설정
    shortest_distance_list[start] = 0
    heapq.heappush(min_heap, (shortest_distance_list[start], start))

    # 다익스트라 연산
    while min_heap:

        weight, node = heapq.heappop(min_heap)
        # 더 짧은 거리로 접근 하였는지 확인
        if weight <= shortest_distance_list[node]:
            shortest_distance_list[node] = weight

            for neighbor, neighbor_weight in m_list[node]:

                if (weight + neighbor_weight <= shortest_distance_list[neighbor]) and (h_list[node] < h_list[neighbor]):
                    shortest_distance_list[neighbor] = weight + neighbor_weight
                    heapq.heappush(min_heap, (shortest_distance_list[neighbor], neighbor))

    return shortest_distance_list


house_sdl = Dijkstra(1)     # 집 -> 산 까지 조건을 만족하는 최단 경로
# print(house_sdl)
korea_sdl = Dijkstra(N)     # 산 -> 고려대 까지 조건을 만족하는 최단 경로
# print(korea_sdl)

max_answer = INF
min_distance = INF
min_index = 0
for i in range(N + 1):

    # 조건을 만족하는 경로가 존재 하는 경우
    if house_sdl[i] != float('inf') and korea_sdl[i] != float('inf'):

        distance_sum = (korea_sdl[i] + house_sdl[i]) * D
        achievement = h_list[i] * E

        if max_answer == INF:   # 초기값인 경우
            max_answer = achievement - distance_sum
        else:
            max_answer = max(max_answer, achievement - distance_sum)

if max_answer == INF:   # 조건을 만족 하는 집 -> 산 -> 고려대 경로가 없는 경우
    print("Impossible")
else:
    print(max_answer)