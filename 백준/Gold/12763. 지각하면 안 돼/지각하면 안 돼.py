import sys
import heapq

N = int(sys.stdin.readline().strip())
T, M = map(int, sys.stdin.readline().strip().split())
L = int(sys.stdin.readline().strip())

m_list = [[] for _ in range(N + 1)]
for _ in range(L):  # 간선 정보 저장
    node1, node2, time, money = map(int, sys.stdin.readline().split())

    m_list[node1].append((node2, time, money))
    m_list[node2].append((node1, time, money))

INF = float('inf')
time_list = [INF for _ in range(N + 1)]
min_heap = []

time_list[1] = 0
heapq.heappush(min_heap, (0, 0, 1))
min_cost = INF
while min_heap:

    time, money, node = heapq.heappop(min_heap)

    if time_list[node] <= T and money <= M:
        time_list[node] = time

        if node == N:
            min_cost = min(min_cost, money)

        for n_node, n_time, n_money in m_list[node]:

            if n_time + time <= T and money + n_money <= M:
                time_list[n_node] = time + n_time
                heapq.heappush(min_heap, (n_time + time, n_money + money, n_node))

if min_cost == INF:
    print(-1)
else:
    print(min_cost)