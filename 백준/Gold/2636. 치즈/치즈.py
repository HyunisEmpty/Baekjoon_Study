import sys
from collections import deque

y_limit, x_limit = map(int, sys.stdin.readline().split())
y_limit += 2
x_limit += 2
bfs_deque = deque([])
deque_cheese = deque([])
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
matrix = []

for i in range(y_limit):
    if i == 0:
        matrix.append([0 for _ in range(x_limit)])
    elif i == y_limit - 1:
        matrix.append([0 for _ in range(x_limit)])
    else:
        matrix.append([0] + list(map(int, sys.stdin.readline().split())) + [0])

past_remove_cheese_counter = 0
hour = 0
while True:

    # 가장 좌측 상단에 있는 칸을 초기값으로 지정한다.
    bfs_set = set()
    bfs_deque.append((0, 0))
    bfs_set.add((0, 0))

    while len(bfs_deque) != 0:
        y, x = bfs_deque.popleft()

        for i in range(4):
            # 현재 좌표를 기준으로 상하좌우 좌표를 만든다.
            ny, nx = dy[i] + y, dx[i] + x
            # 새로운 좌표가 인덱스 범위 안이며, 접근한적 없다면
            if 0 <= ny < y_limit and 0 <= nx < x_limit and (ny, nx) not in bfs_set:
                # 접근했다는것을 확인하기 위해(ny, nx)를 bfs_set에 추가
                bfs_set.add((ny, nx))
                if matrix[ny][nx] == 0:
                    bfs_deque.append((ny, nx))
                else:
                    deque_cheese.append((ny, nx))

    remove_cheese_counter = 0
    while len(deque_cheese) != 0:
        y, x = deque_cheese.popleft()
        matrix[y][x] = 0
        remove_cheese_counter += 1

    if remove_cheese_counter == 0:
        break
    else:
        past_remove_cheese_counter = remove_cheese_counter
        remove_cheese_counter = 0

    hour += 1

print(hour)
print(past_remove_cheese_counter)