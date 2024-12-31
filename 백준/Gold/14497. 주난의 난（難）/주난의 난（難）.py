import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

cnt_list = [[0 for y in range(m)] for x in range(n)]    # 파동이 접근하는데 부서야 하는 최소 벽의 개수
map_list = []       # 벽과 주난이와 범인의 위치에 대한 지도
for _ in range(n):
    map_list.append(list(map(str, sys.stdin.readline().strip())))

queue = deque()
queue.append((x1, y1))
cnt_list[x1][y1] = 1
while queue:

    x, y = queue.popleft()

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:   # 상하좌우 접근

        nx, ny = x + dx, y + dy # 상하좌우 새로운 좌표

        if 0 <= nx < n and 0 <= ny < m:     # 좌표가 그래프 범위 내에 있는지 확인

            if map_list[nx][ny] == '1':     # 벽인 경우

                # 처음 접근 하거나, 더 작은 값으로 접근하는 경우
                if cnt_list[nx][ny] > cnt_list[x][y] + 1 or cnt_list[nx][ny] == 0:
                    cnt_list[nx][ny] = cnt_list[x][y] + 1
                    queue.append((nx, ny))

            else:   # 빈 공간인 경우

                # 처음 접근 하거나, 더 작은 값으로 접근하는 경우
                if cnt_list[nx][ny] > cnt_list[x][y] or cnt_list[nx][ny] == 0:
                    cnt_list[nx][ny] = cnt_list[x][y]
                    queue.append((nx, ny))

#     for i in range(n):
#         print(cnt_list[i])
#
# for i in range(n):
#     print(cnt_list[i])

print(cnt_list[x2][y2])


