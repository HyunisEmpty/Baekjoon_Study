import sys
import heapq

test_case = int(sys.stdin.readline().strip())
for test in range(test_case):

    # n : 노드의 수, m : 간선의 수
    n, m = map(int, sys.stdin.readline().split())

    n_list = [[] for _ in range(n + 1)]     # 간선 사이 정보 입력
    min_heap = []                           # 최소 힙 입력

    # 노드 사이의 간선 정보 입력
    for _ in range(m):

        node1, node2, weight = map(int, sys.stdin.readline().split())

        n_list[node1].append((node2, weight))
        n_list[node2].append((node1, weight))

    k = int(sys.stdin.readline().strip())
    k_list = list(map(int, sys.stdin.readline().split()))

    def Dijkstra(start_node):

        INF = int(1e9)
        shortest_distance_list = [INF for _ in range(n + 1)]    # 최단 거리 테이블

        heapq.heappush(min_heap, (0, start_node))
        while min_heap:

            weight, node = heapq.heappop(min_heap)

            if weight < shortest_distance_list[node]:

                shortest_distance_list[node] = weight

                for neighbor, neighbor_weight in n_list[node]:

                    if neighbor_weight + weight < shortest_distance_list[neighbor]:
                        heapq.heappush(min_heap, (neighbor_weight + weight, neighbor))

        sum_distance = 0
        # print(k_list)
        # print(shortest_distance_list)
        for k_i in k_list:  # 친구들의 방까지의 거리를 저장
            sum_distance += shortest_distance_list[k_i]

        # 현재 방 번호와 해당 방부터 친구들이 있는 방의 번호를 출력
        # print(sum_distance)
        return sum_distance

    min_sum_distance = -1
    min_sum_list = []
    for start_node in range(1, n + 1):

        sum_distance = Dijkstra(start_node)

        if min_sum_distance == -1:
            min_sum_distance = sum_distance
            min_sum_list = [start_node]
        else:
            if min_sum_distance == sum_distance:
                min_sum_list.append(start_node)
            elif min_sum_distance > sum_distance:
                min_sum_distance = sum_distance
                min_sum_list = [start_node]

    min_sum_list.sort()

    print(min_sum_list[0])