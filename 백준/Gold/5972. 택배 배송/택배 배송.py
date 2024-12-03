import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
n_list = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
min_heap = []

INF = int(1e9)
shortestDistanceList = [INF for _ in range(n + 1)]

for _ in range(m):
    node1, node2, weight = map(int, sys.stdin.readline().split())

    n_list[node1].append((node2, weight))
    n_list[node2].append((node1, weight))

shortestDistanceList[1] = 0
heapq.heappush(min_heap, (shortestDistanceList[1], 1))

while min_heap:

    weight, node = heapq.heappop(min_heap)

    # 서로 다른 두 노드 사이에 간선이 1개 이상이라면, 방문 했더라도 가중치가 더 적다면 방문할 수 있다.
    if not visited[node] or weight < shortestDistanceList[node]:

        visited[node] = True
        shortestDistanceList[node] = weight

        for neighbor, neighborWeight in n_list[node]:

            if not visited[neighbor]:
                heapq.heappush(min_heap, (neighborWeight + weight, neighbor))

print(shortestDistanceList[n])