import heapq
import sys
import math

N, W = map(int, sys.stdin.readline().split())
M = float(sys.stdin.readline().strip())

n_list = [(-1, -1)]     # 각 발전소의 좌표
for _ in range(1, N + 1):
    x, y = map(int, sys.stdin.readline().split())

    n_list.append((x, y))

w_list = [set() for _ in range(N + 1)]     # 이미 연결되어 전선이 연결된 발전소
for _ in range(W):
    node1, node2, = map(int, sys.stdin.readline().split())

    w_list[node1].add(node2)
    w_list[node2].add(node1)

min_heap = []
distance_list = [float('inf') for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

distance_list[1] = 0
heapq.heappush(min_heap, (distance_list[1], 1))
while min_heap:

    weight, node = heapq.heappop(min_heap)
    # print(node, distance_list)
    # print(visited)

    if weight <= distance_list[node] and not visited[node]:
        distance_list[node] = weight
        visited[node] = True

        for neighbor in range(1, N + 1):
            if node == neighbor or visited[neighbor]:  # 서로 같은 좌표에 대한 연산인 경우 연산을 하지 않는다.
                continue

            if neighbor in w_list[node]:  # 전선이 이미 연결된 경우
                distance = 0
            else:  # 전선을 새로 만드는 경우
                x1, y1 = n_list[node]
                x2, y2 = n_list[neighbor]
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)   # node1과 node2사이의 거리 저장
            # print("   ", node, neighbor, distance)
            if distance > M:  # 전선의 길이가 제한 길이를 넘어가는 경우
                continue

            if distance + weight <= distance_list[neighbor]:
                distance_list[neighbor] = distance + weight
                heapq.heappush(min_heap, (distance_list[neighbor], neighbor))


print(int(distance_list[N] * 1000))