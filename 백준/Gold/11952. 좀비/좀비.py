import sys
import heapq
from collections import deque

N, M, K, S = map(int, sys.stdin.readline().split())
P, Q = map(int, sys.stdin.readline().split())
K_list = [int(sys.stdin.readline().strip()) for _ in range(K)]
M_list = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]


def Graph():    # 그래프 생성 함수

    graph = [[] for _ in range(N + 1)]

    for node1, node2 in M_list:     # 노드 사이 간선 생성(양방향)
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph


def Find_Zombie_Land(graph):     # 숙박비를 계산하는 함수

    zombie_land = [0] * (N + 1)

    for start in K_list:    # 점령된 도시 접근
        lands = BFS(start, graph, S)
        for land in lands: # 위험 도시의 숙박비를 Q로 변경
            zombie_land[land] = 1

    # 시작 노드와 종료 노드의 숙박비는 0원
    zombie_land[1] = 0
    zombie_land[N] = 0

    return zombie_land


def BFS(start, graph, move_limit):     # 점령 도시 주변 위험 도시 정보 출력 함수

    visit_list = [0] * (N + 1)
    queue = deque()

    ret = []
    visit_list[start] = 1
    queue.append([start, 0])

    while queue:

        node, move = queue.popleft()

        if move > move_limit:
            continue
        else:
            ret.append(node)

        for neighbor in graph[node]:
            if not visit_list[neighbor]:
                visit_list[neighbor] = 1
                queue.append([neighbor, move + 1])

    return ret


def Dijkstra(graph, zombie_land):

    min_heap = []
    INF = float('inf')
    sdl = [INF for _ in range(N + 1)]

    sdl[1] = 0
    heapq.heappush(min_heap, [0, 1])

    while min_heap:

        cost, node = heapq.heappop(min_heap)

        if sdl[node] < cost:
            continue

        for neighbor in graph[node]:

            if neighbor in K_list:
                continue

            next_cost = cost + (Q if zombie_land[neighbor] else P)
            if next_cost < sdl[neighbor]:
                sdl[neighbor] = next_cost
                heapq.heappush(min_heap, [next_cost, neighbor])
    return sdl[N] - P


def Solution():

    graph = Graph()
    zombie_land = Find_Zombie_Land(graph)
    answer = Dijkstra(graph, zombie_land)

    return answer


print(Solution())


