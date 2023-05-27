import sys
from collections import deque

input_x, input_y, input_h = map(int, sys.stdin.readline().split())
matrix = [[list(map(int, sys.stdin.readline().split())) for _ in range(input_y)] for _ in range(input_h)]
queue = deque()
delta_coordinate = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
res = 0

for h in range(input_h):
    for y in range(input_y):
        for x in range(input_x):
            if matrix[h][y][x] == 1:
                queue.append([h, y, x])

while queue:

    h, y, x = queue.popleft()

    for i in range(6):
        delta_h, delta_y, delta_x = delta_coordinate[i]
        new_h, new_y, new_x = delta_h + h, delta_y + y, delta_x + x
        if 0 <= new_h < input_h and 0 <= new_y < input_y and 0 <= new_x < input_x and matrix[new_h][new_y][new_x] == 0:
            matrix[new_h][new_y][new_x] = matrix[h][y][x] + 1
            queue.append([new_h, new_y, new_x])

flag = False
for h_level in matrix:
    for y_level in h_level:
        if 0 in y_level:
            res = 0
            flag = True
            break
        res = max(res, max(y_level))
    if flag:
        break
print(res - 1)