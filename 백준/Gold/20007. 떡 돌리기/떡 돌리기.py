import sys
import heapq

N, M, X, Y = map(int, sys.stdin.readline().split())

m_list = [[] for _ in range(N)]
for _ in range(M):
    node1, node2, weight = map(int, sys.stdin.readline().split())

    m_list[node1].append((weight, node2))
    m_list[node2].append((weight, node1))

def Dijkstra(start):

    min_heap = []   # 최소 힙
    distance_list = [float('inf') for _ in range(N)]    # 최간 거리 테이블

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


time_list = Dijkstra(Y)
for i in range(N):
    time_list[i] = time_list[i] * 2
time_list.sort()

day = 1
day_time = X
for time in time_list:

    if time <= X:    # 떡을 돌릴 수 있는 경우
        if day_time - time >= 0:     # 떡을 돌리고 시간이 남는 경우
            day_time -= time
        else:                       # 떡을 돌릴 시간이 없는 경우
            day += 1
            day_time = X
            day_time -= time
    else:           # 떡을 돌릴 수 없는 경우
        day = -1
        break

print(day)