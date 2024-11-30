import sys
import heapq

n = int(sys.stdin.readline().strip())   # 도시의 개수
m = int(sys.stdin.readline().strip())   # 버스의 개수

n_list = [[] for _ in range(n + 1)]     # 간선 정보 저장
for _ in range(m):
    start, end, distance = map(int, sys.stdin.readline().split())
    n_list[start].append((end, distance, []))   # start에서 end로 가는 비용을 start 인덱스에 저장

start_city, end_city = map(int, sys.stdin.readline().split())   # 시작, 도착 도시

INF = int(1e9)
shortest_distance_list = [INF for _ in range(n + 1)]    # 최단 거리 테이블
shortest_path_list = [[] for _ in range(n + 1)]         # 최단 거리 경로 저장

min_heap = []   # 최소 힙
n_set = set()   # 도시 방문 여부 저장

shortest_distance_list[start_city] = 0
shortest_path_list[start_city].append(start_city)       # 경로에는 출발 도시 포함
heapq.heappush(min_heap, (shortest_distance_list[start_city], start_city, shortest_path_list[start_city]))
while min_heap:

    distance, city, path_list = heapq.heappop(min_heap)

    if city not in n_set:       # 방문 여부 확인,  city로 가는 최단 거리, distance, 최단 경로 path_list인 경우
        n_set.add(city)                             # 방문 여부 저장
        shortest_distance_list[city] = distance     # shortest_distance_list update
        shortest_path_list[city] = path_list        # shortest_path_list update
        for neighbor, neighbor_distance, neighbor_path in n_list[city]:

            if neighbor not in n_set:   # 해당 이웃의 최단 거리가 결정되지 않은 경우
                
                neighbor_path = shortest_path_list[city] + [neighbor]
                heapq.heappush(min_heap, (distance + neighbor_distance, neighbor, neighbor_path))

print(shortest_distance_list[end_city])
print(len(shortest_path_list[end_city]))
print(" ".join(map(str, shortest_path_list[end_city])))