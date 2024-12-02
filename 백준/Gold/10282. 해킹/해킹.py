import sys
import heapq

testCase = int(sys.stdin.readline().strip())

for test in range(testCase):

    n, d, c = map(int, sys.stdin.readline().split())    # n은 노드, d는 간선, c는 시작 노드
    n_list = [[] for i in range(n + 1)]                 # 노드 사이 간선 정보를 저장

    INF = int(1e9)
    minDistanceList = [INF for _ in range(n + 1)]           # 최단 거리 테이블

    min_heap = []                                       # 최소 힙
    visited = [False for _ in range(n + 1)]             # 방문 여부 저장

    for _ in range(d):      # 간선 정보 저장
        end, start, weight = map(int, sys.stdin.readline().split())
        n_list[start].append((end, weight))

    minDistanceList[c] = 0
    heapq.heappush(min_heap, (minDistanceList[c], c))    # 시작 노드 저장

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if not visited[node]:       # 방문 여부 확인

            visited[node] = True
            minDistanceList[node] = weight

            for neighbor, neighbor_weight in n_list[node]:  # 연결된 노드 접근

                if not visited[neighbor]:   # 방문 여부 확인
                    heapq.heappush(min_heap, (neighbor_weight + weight, neighbor))

    cnt = 0
    max_time = 0
    for node in range(1, n + 1):
        if minDistanceList[node] != INF:
            cnt += 1
            max_time = max(max_time, minDistanceList[node])

    print(cnt, max_time)