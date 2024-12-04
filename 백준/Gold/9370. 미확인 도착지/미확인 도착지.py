import sys
import heapq


def Dijkstra(startNode, shortestDistanceList):

    global n_list

    min_heap = []  # 최소힙
    visited = [False for _ in range(n + 1)]  # 해당 노드 방문 여부 저장

    shortestDistanceList[startNode] = 0  # 초기값 정의
    heapq.heappush(min_heap, (shortestDistanceList[startNode], startNode))  # 최소 힙 초기값 정의
    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if not visited[node]:  # 방문하지 않은 경우

            visited[node] = True
            shortestDistanceList[node] = weight

            for neighbor, neighborWeight in n_list[node]:

                if not visited[neighbor]:  # 방문하지 않은 경우

                    heapq.heappush(min_heap, (neighborWeight + weight, neighbor))

    return shortestDistanceList


testCase = int(sys.stdin.readline().strip())

for test in range(testCase):
    # n : 노드의 수, e : 간선의 수, t : 목적지 후보 수
    n, e, t = map(int, sys.stdin.readline().strip().split())
    # start_node : 시작 노드, (g,h) : 반드시 지나야 하는 경로
    startNode, g, h = map(int, sys.stdin.readline().strip().split())

    INF = int(1e9)

    # 노드 사이 간선 정보 저장
    n_list = [[] for _ in range(n + 1)]
    GtoH = 0
    for _ in range(e):  # 간선 정보 저장
        node1, node2, weight = map(int, sys.stdin.readline().strip().split())

        # 양 방향 간선(도로) 정보 저장, (도착 노드, 가중치)
        n_list[node1].append((node2, weight))
        n_list[node2].append((node1, weight))

        # g와 h 사이의 간선이 주어진다면 이를 저장한다.
        if node1 == g and node2 == h:
            GtoH = weight
        elif node1 == h and node2 == g:
            GtoH = weight

    # 목적지 후보 리스트
    t_list = []
    for _ in range(t):
        t_list.append(int(sys.stdin.readline().strip()))
    t_list.sort()

    # 시작 노드 부터 각 노드까지의 최단 거리
    startShortestDistanceList = Dijkstra(startNode, [INF for _ in range(n + 1)])
    # 노드 g 부터 각 노드까지의 최단 거리
    gShortestDistanceList = Dijkstra(g, [INF for _ in range(n + 1)])
    # 노드 h 부터 각 노드까지의 최단 거리
    hShortestDistanceList = Dijkstra(h, [INF for _ in range(n + 1)])

    answer_list = []

    for t_node in t_list:   # 목적지 후보

        shortestDistance = 0

        # 시작 노드에서 g에 먼저 도착하는 경우
        if startShortestDistanceList[g] < startShortestDistanceList[h]:
            shortestDistance = startShortestDistanceList[g] + GtoH + hShortestDistanceList[t_node]
        else:
            shortestDistance = startShortestDistanceList[h] + GtoH + gShortestDistanceList[t_node]

        if shortestDistance == startShortestDistanceList[t_node]:
            answer_list.append(t_node)

    print(" ".join(map(str, answer_list)))