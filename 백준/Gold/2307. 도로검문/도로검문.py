import sys
import heapq
from collections import deque

n, m = map(int, sys.stdin.readline().split())           # 노드와 간선의 개수 저장

INF = float('inf')
n_list = [[] for _ in range(n + 1)]                     # 노드 사이 간선 정보 저장
min_heap = []                                           # 최소 힙

for _ in range(m):      # 간선 정보 저장

    node1, node2, weight = map(int, sys.stdin.readline().split())

    # 양 방향 간선
    n_list[node1].append((node2, weight))
    n_list[node2].append((node1, weight))

def ShortestPath():

    shortest_distance_list = [INF for _ in range(n + 1)]  # 최단거리 테이블

    shortest_distance_list[1] = 0
    parent_list = [[] for _ in range(n + 1)]
    heapq.heappush(min_heap, (shortest_distance_list[1], 1, 1))

    while min_heap:

        weight, node, before_node = heapq.heappop(min_heap)

        if weight <= shortest_distance_list[node]:

            shortest_distance_list[node] = weight

            if before_node != node:
                parent_list[node].append(before_node)

            for neighbor, neighbor_weight in n_list[node]:

                if neighbor_weight + weight <= shortest_distance_list[neighbor]:

                    shortest_distance_list[neighbor] = neighbor_weight + weight
                    heapq.heappush(min_heap, (shortest_distance_list[neighbor], neighbor, node))

    return shortest_distance_list[n], parent_list


def Dijkstra(node1, node2):

    shortest_distance_list = [INF for _ in range(n + 1)]  # 최단거리 테이블

    shortest_distance_list[1] = 0
    heapq.heappush(min_heap, (shortest_distance_list[1], 1))

    while min_heap:

        weight, node = heapq.heappop(min_heap)

        if weight <= shortest_distance_list[node]:

            shortest_distance_list[node] = weight

            for neighbor, neighbor_weight in n_list[node]:

                # node1, node2 간선을 배제
                if (node == node1 and neighbor == node2) or (node == node2 and neighbor == node1):
                    continue

                if neighbor_weight + weight <= shortest_distance_list[neighbor]:

                    shortest_distance_list[neighbor] = neighbor_weight + weight
                    heapq.heappush(min_heap, (shortest_distance_list[neighbor], neighbor))

    return shortest_distance_list[n]


min_distance, parent_list = ShortestPath()

# print(parent_list)
# print(min_distance)

queue = deque()                         # 자료구조 큐 선언
visited_set = set()                     # 도착 노드는 이미 접근

# 도착 노드 N까지 이어지는 최단 경로를 저장
for parent in parent_list[n]:
    visited_set.add((n, parent))                      # n의 방문 여부 체크
    queue.append((n, parent))       # 도착노드와 그에 연결된 최단 경로의 노드

# 지연 시킬 수 있는 최대 시간을 저장
answer = 0
while queue:

    son, parent = queue.popleft()
    visited_set.add((son, parent))                        # 도착 노드에 연결된 최단 거리 상의 노드
    now_distance = Dijkstra(son, parent)                    # 현재 차단한 경로에 대한 최단거리

    if now_distance != INF:
        answer = max(answer, now_distance - min_distance)
    else:
        answer = -1
        break
    # print("차단한 거리 :", son, parent)
    # print("현재 최단 경로 :", now_distance)

    for grand_parent in parent_list[parent]:
        if (parent, grand_parent) not in visited_set:
            queue.append((parent, grand_parent))

print(answer)