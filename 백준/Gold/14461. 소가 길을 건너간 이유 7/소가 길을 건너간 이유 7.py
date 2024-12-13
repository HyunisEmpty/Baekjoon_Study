import sys
from collections import deque

n, t = map(int, sys.stdin.readline().split())  # n : 노드의 개수, t : 간선의 가중치
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

INF = int(1e9)
shortest_distance_list = [[[INF, INF, INF] for i in range(n)] for j in range(n)]


queue = deque()  # 큐 자료구조 정의
queue.append((0, 0, 0, 0))
shortest_distance_list[0][0][0] = 0

while queue:

    x, y, weight, cnt = queue.popleft()

    if x == n - 1 and y == n - 1:  # 도착 지점인 경우 : 더이상 연산을 할 필요가 없다.
        shortest_distance_list[x][y][cnt] = min(weight, shortest_distance_list[x][y][cnt])
    else:
        next_cnt = cnt + 1

        if next_cnt == 3:
            next_cnt = 0

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:  # 2차원 배열 입력 범위 안에 있는지 확인

                if next_cnt == 0:
                    new_weight = weight + t + n_list[nx][ny]
                else:
                    new_weight = weight + t

                if new_weight < shortest_distance_list[nx][ny][next_cnt]:
                    shortest_distance_list[nx][ny][next_cnt] = new_weight
                    queue.append((nx, ny, new_weight, next_cnt))

print(min(shortest_distance_list[n - 1][n - 1]))