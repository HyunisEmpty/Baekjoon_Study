import sys
import heapq
from collections import defaultdict, deque

while True:

    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    start_node, end_node = map(int, sys.stdin.readline().split())

    INF = int(1e9)
    n_list = [[] for _ in range(n)]         # 이웃 노드 정보 저장
    parent = defaultdict(list)              # 노드의 경로를 저장
    parent_list = [0 for _ in range(n)]     # 자신에게 연결된 역추적 간선의 개수를 저장
    queue_set = set()                       # 큐에 들어가 있는 원소 확인

    # 간선 정보 입력
    for _ in range(m):
        u, v, p = map(int, sys.stdin.readline().split())
        n_list[u].append((v, p))

    # 각 노드 까지 최단 거리로 접근하는 모든 경로가 parent초기화
    def FirstDijkstra():

        shortest_distance_list = [INF] * n              # 최단거리 테이블
        min_heap = []                                   # 최소 힙

        shortest_distance_list[start_node] = 0
        heapq.heappush(min_heap, (0, start_node))
        while min_heap:

            weight, node = heapq.heappop(min_heap)      # 현재 노드 접근

            if weight > shortest_distance_list[node]:   # 최단 경로가 아닌 경우
                continue

            for neighbor, neighbor_weight in n_list[node]:

                # 새로운 최단 경로가 생긴 경우 : 기존에 neighbor에 접근했던 노드는 최단 경로가 아니므로 초기화
                if neighbor_weight + weight < shortest_distance_list[neighbor]:
                    parent[neighbor] = [node]   # node에서 neighbor로 연결된 간선 생성
                    shortest_distance_list[neighbor] = neighbor_weight + weight
                    heapq.heappush(min_heap, (neighbor_weight + weight, neighbor))
                    parent_list[node] += 1          # node -> neighbor로 이어지는 최단 거리 간선 저장

                # 기존 최단 거리와 동일한 길이의 새로운 경로가 생긴 경우 : 이전 노드를 neighbor에 저장
                elif neighbor_weight + weight == shortest_distance_list[neighbor]:
                    parent[neighbor].append(node)
                    parent_list[node] += 1          # node -> neighbor로 이어지는 최단 거리 간선 저장

        # print(parent_list)
        return shortest_distance_list[end_node]

    # 최단 경로를 n_list에서 제거
    def remove_shortest_path():
        queue = deque([end_node])   # end_node 부터 최단경로 역 추적
        while queue:
            parent_node = queue.popleft()  # 현재 노드
            queue_set.add(parent_node)
            # print(parent_node)
            for son_node in parent[parent_node]:
                # print(son_node)
                if parent_list[son_node] != 0:
                    # 자식 노드에서 부모 노드로 최단 거리로 접근하는 경우를 제외
                    n_list[son_node] = [(v, p) for v, p in n_list[son_node] if v != parent_node]
                    # print(parent_node, n_list[son_node])
                    queue.append(son_node)
                    parent_list[son_node] -= 1
                    # queue_set.add(son_node)
        # print(queue_set)
        # for info in n_list:
            # print(info)

    def SecondDijkstra():

        shortest_distance_list = [INF] * n  # 최단거리 테이블
        min_heap = []  # 최소 힙

        shortest_distance_list[start_node] = 0
        heapq.heappush(min_heap, (0, start_node))
        while min_heap:

            weight, node = heapq.heappop(min_heap)  # 현재 노드 접근

            for neighbor, neighbor_weight in n_list[node]:

                # 새로운 최단 경로가 생긴 경우 : 기존에 neighbor에 접근했던 노드는 최단 경로가 아니므로 초기화
                if neighbor_weight + weight < shortest_distance_list[neighbor]:

                    shortest_distance_list[neighbor] = neighbor_weight + weight
                    heapq.heappush(min_heap, (neighbor_weight + weight, neighbor))

        # print(shortest_distance_list)
        return shortest_distance_list[end_node]

    FirstDijkstra()
    remove_shortest_path()
    second_shortest_distance = SecondDijkstra()

    if second_shortest_distance == INF:
        print(-1)
    else:
        print(second_shortest_distance)