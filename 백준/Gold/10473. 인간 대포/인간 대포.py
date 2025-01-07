import sys
import heapq
import math

start_x, start_y = map(float, sys.stdin.readline().split())       # 시작 지점
end_x, end_y = map(float, sys.stdin.readline().split())           # 종료 지점

v_list = [0]                            # 정점의 위치 저장
v_list.append((start_x, start_y))
v_list.append((end_x, end_y))

n = int(sys.stdin.readline().strip())   # 대포의 수 => 출발점과 도착점을 제외한 노드의 수
for _ in range(n):

    x, y = map(float, sys.stdin.readline().split())
    v_list.append((x, y))

e_list = [[] for _ in range(n + 3)]     # 간선의 정보 저장 ( 연결된 노드, 시간 )
for i in range(1, n + 3):

    x, y = v_list[i]

    for j in range(1, n + 3):

        nx, ny = v_list[j]

        if j != i:  # 자기 자신에 대한 연산이 아닌 경우
            if i == 1 or i == 2:    # 출발점 도착점인 경우
                distance = math.sqrt((x - nx) ** 2 + (y - ny) ** 2)     # 두 노드 사이의 거리
                time = distance/5                                     # 걸어가는 경우
            else:
                distance = math.sqrt((x - nx) ** 2 + (y - ny) ** 2)  # 걸어서 가는 경우

                if distance <= 30:  # 30이하인 경우 걸어가는 경우가 이득
                    time = distance/5
                elif 30 < distance <= 50:
                    time = 2 + (50 - distance)/5
                else:
                    time = 2 + (distance - 50)/5

            e_list[i].append((j, time))

INF = float('inf')
shortest_distance_list = [INF for _ in range(n + 3)]    # 최단 거리 테이블
min_heap = []

shortest_distance_list[1] = 0
heapq.heappush(min_heap, (shortest_distance_list[1], 1))
while min_heap:

    weight, node = heapq.heappop(min_heap)

    if weight <= shortest_distance_list[node]:

        shortest_distance_list[node] = weight

        for neighbor, neighbor_weight in e_list[node]:

            if neighbor_weight + weight <= shortest_distance_list[neighbor]:
                shortest_distance_list[neighbor] = neighbor_weight + weight
                heapq.heappush(min_heap, (shortest_distance_list[neighbor], neighbor))

print(shortest_distance_list[2])