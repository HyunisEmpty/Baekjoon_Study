import sys

# 도시의 개수
n = int(sys.stdin.readline().strip())
# 도시에 도착에 최단 시간이 저장된 최단 시간 리스트
n_list = [1e9 for i in range(n + 1)]
# 버스의 개수
m = int(sys.stdin.readline().strip())
# 버스의 정보를 저장하는 리스트
m_list = [[] for i in range(n + 1)]
# 해당 도시를 방문한적 있는지에 대한 정보를 저장하는 리스트
visited_list = [False for i in range(n + 1)]

# 모든 버스(간선)의 정보를 입력 받는다.
for i in range(m):

    a, b, c = map(int, sys.stdin.readline().strip().split())
    m_list[a].append((b, c))

# 시작도시와 도착 도시의 정보를 입력 받는다.
start_n, end_n = map(int, sys.stdin.readline().strip().split())

# 최단 거리 테이블 초기화
n_list[start_n] = 0
visited_list[start_n] = True
start_city = start_n
# 시작 도시를 제외한 도시에 대해서 연산 진행
for i in range(n - 1):

    visited_list[start_city] = True

    # print(n_list, start_city)

    # 출발 도시부터 도착 도시의 정보들을 저장
    for bus_info in m_list[start_city]:
        # 각 버스 도착 도시, 비용
        end_city, cost = map(int, bus_info)

        # 비용이 가장 적다면 최단 시간 리스트 업데이트
        if n_list[end_city] > n_list[start_city] + cost:
            n_list[end_city] = n_list[start_city] + cost

    # 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 리스트 인덱스와 값을 찾기 위한 변수
    min_cost = 1e9

    # 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 리스트 선택
    for j in range(len(n_list)):

        # 방문 한적이 없는 경우
        if visited_list[j] == False:
            if n_list[j] < min_cost:
                min_cost = n_list[j]
                start_city = j

print(n_list[end_n])