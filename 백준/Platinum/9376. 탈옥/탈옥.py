from collections import deque
import sys


def BFS(start):

    global h
    global w
    global map_list

    cnt_list = [[float('inf')] * w for _ in range(h)]
    queue = deque()
    queue.append((start[0], start[1]))
    cnt_list[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:

                # 벽이거나, 최단 거리 접근이 아닌 경우
                if map_list[nx][ny] == "*" or cnt_list[nx][ny] <= cnt_list[x][y]:
                    continue

                if map_list[nx][ny] == "#":
                    if cnt_list[nx][ny] > cnt_list[x][y] + 1:
                        cnt_list[nx][ny] = cnt_list[x][y] + 1
                        queue.append((nx, ny))
                else:
                    if cnt_list[nx][ny] > cnt_list[x][y]:
                        cnt_list[nx][ny] = cnt_list[x][y]
                        queue.append((nx, ny))

    return cnt_list

test = int(sys.stdin.readline().strip())

for test_case in range(test):

    h, w = map(int, sys.stdin.readline().split())
    map_list = ['.' * (w + 2)] + ['.' + sys.stdin.readline().strip() + '.' for _ in range(h)] + ['.' * (w + 2)]
    h += 2
    w += 2

    # 죄수의 위치 저장
    prisoners = []
    for x in range(h):
        for y in range(w):
            if map_list[x][y] == '$':
                prisoners.append((x, y))

    distances_0 = BFS((0, 0))           # 감옥 밖 출발
    distances_1 = BFS(prisoners[0])     # 첫 번째 죄수 출발
    distances_2 = BFS(prisoners[1])     # 두 번째 죄수 출발

    min_answer = float('inf')

    for i in range(h):
        for j in range(w):

            # 벽인 경우
            if map_list[i][j] == '*':
                continue

            total_cost = distances_0[i][j] + distances_1[i][j] + distances_2[i][j]

            if map_list[i][j] == '#':
                total_cost -= 2  # 문은 중복 계산 방지

            min_answer = min(min_answer, total_cost)

    print(min_answer)