import sys
import heapq

test = int(sys.stdin.readline().strip())

for test_case in range(test):

    n, m = map(int, sys.stdin.readline().split())       # 노드(M), 간선(N)

    INF = float('inf')
    shortest_distance_list = [INF for _ in range(m)]    # 최단 거리 테이블
    min_heap = []                                       # 최소 힙
    mother_list = [0 for _ in range(m)]                 # 부모 노드의 정보 저장

    m_list = [[] for _ in range(m)]                     # 간선 정보 저장
    for _ in range(n):
        node1, node2, weight = map(int, sys.stdin.readline().split())

        # 양방향 경로 저장
        m_list[node1].append((node2, weight))
        m_list[node2].append((node1, weight))

    # 현신이의 위치 에서 시작
    shortest_distance_list[0] = 0
    heapq.heappush(min_heap, (shortest_distance_list[0], 0, 0))

    while min_heap:

        weight, node, mother_node = heapq.heappop(min_heap)  # 현재 최단 거리 추출

        if weight <= shortest_distance_list[node]:
            shortest_distance_list[node] = weight
            mother_list[node] = mother_node

            for neighbor, neighbor_weight in m_list[node]:

                if neighbor_weight + weight <= shortest_distance_list[neighbor]:
                    shortest_distance_list[neighbor] = neighbor_weight + weight
                    heapq.heappush(min_heap, (shortest_distance_list[neighbor], neighbor, node))

    if shortest_distance_list[m-1] == INF:  # 최고위원에게 접근할 수 없는 경우
        print("Case #" + str(test_case + 1) + ":", -1)
    else:
        mother = m - 1
        path_list = []
        while mother != 0:
            path_list.append(mother)
            mother = mother_list[mother]
        path_list.append(mother)
        path_list.reverse()
        answer = " ".join(map(str, path_list))
        print("Case #" + str(test_case + 1) + ":", answer)