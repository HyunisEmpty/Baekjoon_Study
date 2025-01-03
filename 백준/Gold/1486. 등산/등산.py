import sys
from collections import deque

n, m, t, d = map(int, sys.stdin.readline().split()) # 세로, 가로 크기, 최대 높이차, 어두워 지는 시간

queue = deque()
max_height = 0

# 각 문자(키)에 대응하는 높이(값, 정수)를 저장하는 딕셔너리 생성
alphabet_to_nuber = {}
for i in range(26):

    # 문자의 아스키 코드 값에 대응 하는 문자를 저장 'A'-'Z' or 'a'-'z'
    big_letter = chr(ord("A") + i)
    little_letter = chr(ord("a") + i)

    alphabet_to_nuber[big_letter] = i
    alphabet_to_nuber[little_letter] = i + 26

# 산의 높이 정보를 저장하는 리스트 생성, 특정한 곳에 갔다가 돌아오는 시간을 저장하는 리스트 생성, 방문여부 저장 리스트 생성
map_list = []
height_time_list = []   # 올라갈 때 최단 시간
height_visited = []     # 올라갈 때 방문 여부
down_time_list = []     # 내려올 때 최단 시간
down_visited = []       # 내려올 때 방문 여부
sum_time_list = []      # 내려올 때 올라갈 때 최단 시간의 합
for x in range(n):
    map_list.append(list(map(str, sys.stdin.readline().strip())))
    height_time_list.append([0 for _ in range(m)])
    height_visited.append([False for _ in range(m)])
    down_time_list.append([0 for _ in range(m)])
    down_visited.append([False for _ in range(m)])
    sum_time_list.append([0 for _ in range(m)])

    # 문자에 대응하는 높이값으로 지도 초기화
    for y in range(m):
        map_list[x][y] = alphabet_to_nuber[map_list[x][y]]

# print("지도 정보")
# for i in range(n):
#
#     print(map_list[i])
# print("")

# 올라가는 최단 시간 저장
queue.append((0, 0))
height_visited[0][0] = True
while queue:

    x, y = queue.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:   # 상하좌우 접근
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:     # 인덱스 범위 확인

            height_gap = abs(map_list[nx][ny] - map_list[x][y])     # 높이 차 저장
            # print(map_list[x][y], map_list[nx][ny], height_gap)

            # 접근 한적 없으면서 높이 차가 t 이하인 경우
            if not height_visited[nx][ny] and height_gap <= t:

                new_time = height_time_list[x][y]

                if map_list[x][y] < map_list[nx][ny]:       # 올라가는 경우
                    new_time += (height_gap * height_gap)
                elif map_list[x][y] > map_list[nx][ny]:     # 내려가는 경우
                    new_time += 1
                else:                                       # 높이가 같은 경우
                    new_time += 1

                if d >= new_time:       # 어두워 지기 전에 접근 가능한 경우
                    height_visited[nx][ny] = True  # 방문 여부 확인
                    height_time_list[nx][ny] = new_time
                    queue.append((nx, ny))

            # 접근 한적 있는 경우
            elif height_visited[nx][ny] and height_gap <= t:

                new_time = height_time_list[x][y]

                if map_list[x][y] < map_list[nx][ny]:       # 올라가는 경우
                    new_time += (height_gap * height_gap)
                elif map_list[x][y] > map_list[nx][ny]:     # 내려가는 경우
                    new_time += 1
                else:                                       # 높이가 같은 경우
                    new_time += 1

                if height_time_list[nx][ny] > new_time and d >= new_time:  # 더 짧은 시간에 어두워 지기 전에 접근 할 수 있는 경우
                    height_time_list[nx][ny] = new_time
                    queue.append((nx, ny))

# 내려오는 최단 시간 저장
queue.append((0, 0))
down_visited[0][0] = True
while queue:

    x, y = queue.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:   # 상하좌우 접근
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:     # 인덱스 범위 확인

            height_gap = abs(map_list[nx][ny] - map_list[x][y])     # 높이 차 저장

            # 접근 한적 없으면서 높이 차가 t 이하인 경우
            if not down_visited[nx][ny] and height_gap <= t:

                new_time = down_time_list[x][y]

                if map_list[x][y] < map_list[nx][ny]:       # 올라가는 경우
                    new_time += 1
                elif map_list[x][y] > map_list[nx][ny]:     # 내려가는 경우
                    new_time += (height_gap * height_gap)
                else:                                       # 높이가 같은 경우
                    new_time += 1

                if d >= new_time:       # 어두워 지기 전에 접근 가능한 경우
                    down_visited[nx][ny] = True  # 방문 여부 확인
                    down_time_list[nx][ny] = new_time
                    queue.append((nx, ny))

            # 접근 한적 있는 경우
            elif down_visited[nx][ny] and height_gap <= t:

                new_time = down_time_list[x][y]

                if map_list[x][y] < map_list[nx][ny]:  # 올라가는 경우
                    new_time += 1
                elif map_list[x][y] > map_list[nx][ny]:  # 내려가는 경우
                    new_time += (height_gap * height_gap)
                else:  # 높이가 같은 경우
                    new_time += 1

                if down_time_list[nx][ny] > new_time and d >= new_time:  # 더 짧은 시간에 어두워 지기 전에 접근 할 수 있는 경우
                    down_time_list[nx][ny] = new_time
                    queue.append((nx, ny))

max_height = 0
for x in range(n):
    for y in range(m):
        sum_time_list[x][y] += height_time_list[x][y]
        sum_time_list[x][y] += down_time_list[x][y]

        if sum_time_list[x][y] <= d and map_list[x][y] > max_height and (height_visited[x][y] and down_visited[x][y]):
            max_height = map_list[x][y]


# print("")
# for i in range(n):
#     print(sum_time_list[i])

print(max_height)