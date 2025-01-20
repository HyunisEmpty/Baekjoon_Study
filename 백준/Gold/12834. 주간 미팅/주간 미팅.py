import sys
import heapq

N, V, E = map(int, sys.stdin.readline().split())
A, B = map(int, sys.stdin.readline().split())           # 카이스트와 씨알푸드의 위치
n_list = list(map(int, sys.stdin.readline().split()))   # 팀원의 집이 위치

m_list = [[] for _ in range(V + 1)]     # 간선 정보 저장
for _ in range(E):
    node1, node2, weight = map(int, sys.stdin.readline().split())

    m_list[node1].append((weight, node2))
    m_list[node2].append((weight, node1))


def Dijkstra(start):

    min_heap = []   # 최소 힙
    distance_list = [float('inf') for _ in range(V + 1)]    # 최간 거리 테이블

    distance_list[start] = 0
    heapq.heappush(min_heap, (distance_list[start], start))

    while min_heap:

        weight, node = heapq.heappop(min_heap)

        if weight <= distance_list[node]:
            distance_list[node] = weight

            for neighbor_weight, neighbor in m_list[node]:
                if neighbor_weight + weight <= distance_list[neighbor]:
                    distance_list[neighbor] = neighbor_weight + weight
                    heapq.heappush(min_heap, (distance_list[neighbor], neighbor))

    return distance_list

Kist_distance_list = Dijkstra(A)
food_distance_list = Dijkstra(B)

answer = 0
for member_house in n_list:

    # 접근 할 수 없는 경우
    if Kist_distance_list[member_house] == float('inf'):
        answer -= 1
    else:
        answer += Kist_distance_list[member_house]

    if food_distance_list[member_house] == float('inf'):
        answer -= 1
    else:
        answer += food_distance_list[member_house]

print(answer)