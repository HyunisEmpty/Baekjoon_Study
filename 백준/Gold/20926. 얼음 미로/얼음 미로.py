import sys
from collections import deque

W, H = map(int, sys.stdin.readline().split())

heap = deque()  # 힙

direction_dict = dict()
for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    direction_dict[direction] = [[float('inf') for _ in range(W)] for _ in range(H)]

map_list = []       # 지도 정보 저장
for x in range(H):      # 지도 생성
    map_list.append(list(sys.stdin.readline().strip()))

    for y in range(W):      # 상세 위치 저장

        if map_list[x][y] == 'T':   # 시작 지점인 경우
            start_position = (x, y, True, (1, 0))
            map_list[x][y] = '0'
            direction_dict[(1, 0)][x][y] = 0

        if map_list[x][y] == 'E':   # 도착 지점인 경우
            end_position = (x, y)

# BFS 알고리즘
heap.append(start_position)
while heap:

    # 현재 좌표, 운동 상태, 운동 방향이 넘어온다.
    x, y, stop, direction = heap.popleft()

    # 정지한 경우
    if stop:

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:   # 상하좌우 이동
            nx, ny = x + dx, y + dy     # 새로운 좌표 생성
            if 0 <= nx < H and 0 <= ny < W:     # 인덱스 범위 내부인 경우

                next_block = map_list[nx][ny]
                new_direction = (dx, dy)

                # 모든 방향에 대해 현재 방향 값을 저장
                direction_dict[new_direction][x][y] = direction_dict[direction][x][y]

                if next_block == "H":  # 구멍인 경우(추가 연산 x)
                    continue

                elif next_block == "R":  # 돌인 경우(정지 해야 한다)
                    continue

                elif next_block == "E":  # 도착인 경우(새로운 값으로 업데이트
                    if direction_dict[new_direction][nx][ny] > direction_dict[new_direction][x][y]:
                        direction_dict[new_direction][nx][ny] = direction_dict[new_direction][x][y]
                        heap.append((nx, ny, False, new_direction))

                else:   # 얼음인 경우
                    if direction_dict[new_direction][nx][ny] > direction_dict[new_direction][x][y] + int(next_block):
                        direction_dict[new_direction][nx][ny] = direction_dict[new_direction][x][y] + int(next_block)
                        heap.append((nx, ny, False, new_direction))

    # 움직이는 경우
    else:

        nx, ny = x + direction[0], y + direction[1]     # 운동 방향으로 다음에 도착하게 되는 칸
        time_table = direction_dict[direction]

        if 0 <= nx < H and 0 <= ny < W:     # 인덱스 범위 내부인 경우

            next_block = map_list[nx][ny]

            if next_block == "H":       # 구멍인 경우(추가 연산 x)
                continue

            elif next_block == "R":     # 돌인 경우(정지 해야 한다)
                heap.append((x, y, True, direction))

            elif next_block == "E":       # 도착인 경우(새로운 값으로 업데이트
                if time_table[nx][ny] > time_table[x][y]:
                    time_table[nx][ny] = time_table[x][y]
                    heap.append((nx, ny, False, direction))

            else:   # 얼음인 경우

                if time_table[nx][ny] > time_table[x][y] + int(next_block):
                    time_table[nx][ny] = time_table[x][y] + int(next_block)
                    heap.append((nx, ny, False, direction))

answer = float('inf')
for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

    answer = min(answer, direction_dict[direction][end_position[0]][end_position[1]])

if answer == float('inf'):
    print(-1)
else:
    print(answer)
