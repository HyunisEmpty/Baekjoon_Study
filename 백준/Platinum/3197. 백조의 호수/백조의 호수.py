import sys
from collections import deque
import copy

mx, my = map(int, sys.stdin.readline().split())
map_list = [list(sys.stdin.readline().strip()) for _ in range(mx)]
swan_visited = [[False for _ in range(my)] for _ in range(mx)]
ice_visited = [[False for _ in range(my)] for _ in range(mx)]

# 지도 정보 저장및 초기값 저장
ice_queue = deque()     # 다음날 녹게될 얼음의 위치를 저장
swan_queue = deque()    # 백조의 BFS 알고리즘을 위한 queue
for x in range(mx):
    for y in range(my):

        if map_list[x][y] == 'X':       # 현재 위치가 얼음인 경우
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < mx and 0 <= ny < my:
                    if map_list[nx][ny] == '.' or map_list[nx][ny] == "L":     # 얼음 상하좌우에 물이 있는 경우 => 백조가 있는 경우는?
                        ice_queue.append((x, y))
                        ice_visited[x][y] = True
                        break       # 현재 얼음에 대해서 더 이상의 연산은 불 필요 하다

        elif map_list[x][y] == 'L' and len(swan_queue) == 0:     # 현재 위치가 처음 발견한 백조인 경우

            # 백조 BFS 초기값 정의
            swan_queue.append((x, y))
            swan_visited[x][y] = True

swan_meet = False
day_count = 0
next_ice_queue = deque()
next_swan_queue = deque()
while not swan_meet:    # 백조끼리 만날때 까지 무한 반복

        # 백조가 접근 가능한 위치에 BFS 알고리즘실행
        while swan_queue and not swan_meet: # 백조끼리 만나면 연산 중단

            x, y = swan_queue.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < mx and 0 <= ny < my:   # 인덱스 범위 내부에 있는지 판단
                    if map_list[nx][ny] == "." and not swan_visited[nx][ny]:        # 상하좌우칸 중 물이며 방문하지 않은 경우
                        swan_queue.append((nx, ny))
                        swan_visited[nx][ny] = True
                    # 내일 녹아내릴칸 에 대한 연산
                    elif map_list[nx][ny] == "X" and not swan_visited[nx][ny]:      # 상하좌우칸 중 얼음이 있는 경우 => 코드를 이렇게 짜면 집합이 없어도 중복연산 해결 가능
                        next_swan_queue.append((nx, ny))
                        swan_visited[nx][ny] = True
                    elif map_list[nx][ny] == "L" and not swan_visited[nx][ny]:      # 상하좌우 칸 중 백조를 만난 경우
                        swan_meet = True
        for i in range(len(next_swan_queue)):     # 다음날 백조가 갈 위치를 저장
            x, y = next_swan_queue.popleft()
            swan_queue.append((x, y))

        if not swan_meet:   # 스완을 만나지 못한 경우 하루 증가
            day_count += 1

        # 호수의 얼음이 녹음
        while ice_queue and not swan_meet: # 백조끼리 만나면 연산 중단

            x, y = ice_queue.popleft()
            map_list[x][y] = '.'        # 현재 얼음이 있던 곳을 녹아서 물로 변경

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < mx and 0 <= ny < my:
                    if map_list[nx][ny] == "X" and not ice_visited[nx][ny]: # 현재 녹은 얼음 상하좌우에 얼음이 있는 경우
                        next_ice_queue.append((nx, ny))
                        ice_visited[nx][ny] = True
        for i in range(len(next_ice_queue)):     # 다음날 얼음이 녹을 위치 저장
            x, y = next_ice_queue.popleft()
            ice_queue.append((x, y))

print(day_count)