import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
E_list = [[] for _ in range(V + 1)]

MST_weight = 0
min_heap = []
heapq.heappush(min_heap, (0, 1))
vertex_set = set()

# 간선 정보 저장
for _ in range(E):
    v1, v2, weight = map(int, sys.stdin.readline().split())
    E_list[v1].append((v2, weight))
    E_list[v2].append((v1, weight))

# 1번 노드 부터 접근
while min_heap:
    weight, vertex = heapq.heappop(min_heap)

    if vertex not in vertex_set:
        MST_weight += weight
        vertex_set.add(vertex)

        # 현재 정점과 연결된 주변 정점과의 간선의 정보
        for next_vertex, next_weight in E_list[vertex]:

            # 아직 접근 한적 없는 간선인 경우
            if next_vertex not in vertex_set:
                heapq.heappush(min_heap, (next_weight, next_vertex))

print(MST_weight)