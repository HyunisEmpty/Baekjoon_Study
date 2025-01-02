import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

garbage_set = set()         # 쓰레기 위치 저장
garbage_side_set = set()    # 쓰레기 주변 위치 저장
start_position = 0          # 시작 위치 저장
end_position = 0            # 종료 위치 저장
queue = deque()             # 자료구조 큐

cnt_list = []               # 쓰레기 옆을 지나온 횟수, 쓰레기를 지나온 횟수 순으로 저장
visited = []                # 방문 여부를 저장
for i in range(n):

    cnt_list.append([])
    visited.append([])

    for j in range(m):
        cnt_list[i].append([0, 0])
        visited[i].append(False)

# 지도의 정보를 저장하는 리스트
map_list = []
for x in range(n):
    map_list.append(list(map(str, sys.stdin.readline().strip())))

    for y in range(m):

        # 시작 위치 저장
        if map_list[x][y] == "S":
            start_position = (x, y)

        # 쓰레기 위치 저장
        elif map_list[x][y] == "g":
            map_list[x][y] = "G"
            garbage_set.add((x, y))

        # 꽃의 위치
        elif map_list[x][y] == "F":
            end_position = (x, y)

for gx, gy in garbage_set:

    # # 쓰레기 상하좌우 쓰레기를 지나가는 위치 저장
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = gx + dx, gy + dy

        if 0 <= nx < n and 0 <= ny < m:

            # 비어있고 인접한 칸이 쓰레기인 경우만 이에 해당 한다.
            if map_list[nx][ny] == ".":
                map_list[nx][ny] = "g"


queue.append(start_position)    # 큐 초기값 지정
while queue:

    x, y = queue.popleft()

    # print(x, y)
    # for i in range(n):
    #     print(cnt_list[i])
    # print("")

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:   # 상하좌우 접근
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:                 # 새로운 좌표가 인덱스 범위 내에 있는지 확인

            new_b, new_c = cnt_list[x][y][0], cnt_list[x][y][1]

            if map_list[nx][ny] == "g":  # 쓰레기 옆을 지나가는 경우
                new_b += 1
            elif map_list[nx][ny] == "G":  # 쓰레기를 지나가는 경우
                new_c += 1

            # 접근한 적이 없다면
            if not visited[nx][ny]:

                visited[nx][ny] = True     # 접근 표시
                cnt_list[nx][ny][0] = new_b
                cnt_list[nx][ny][1] = new_c

                queue.append((nx, ny))

            # 접근한 적이 있는 경우
            else:

                # 인접한 칸보다 C가 작다면 접근 O
                if cnt_list[nx][ny][1] > new_c:
                    cnt_list[nx][ny][0] = new_b
                    cnt_list[nx][ny][1] = new_c
                    queue.append((nx, ny))

                # 인접한 칸과 C가 같다면
                elif cnt_list[nx][ny][1] == new_c:

                    # 인접한 칸보다 b가 작다면 접근
                    if cnt_list[nx][ny][0] > new_b:
                        cnt_list[nx][ny][0] = new_b
                        cnt_list[nx][ny][1] = new_c
                        queue.append((nx, ny))

end_x, end_y = end_position
b, c = cnt_list[end_x][end_y]
print(c, b)