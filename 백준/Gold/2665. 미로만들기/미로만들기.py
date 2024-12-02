import sys
from collections import deque

n = int(sys.stdin.readline().strip())                       # 방의 수 저장
nList = [sys.stdin.readline().strip() for _ in range(n)]    # 방의 정보 저장

minDelBlackRoomList = [[0 for x in range(n)] for y in range(n)]     # 접근을 위해서 최소로 변경해야 하는 검은 방의 수 저장 리스트
visited = [[False for x in range(n)] for y in range(n)]             # 방문 여부를 저장하는 리스트

queue = deque()     # 큐 자료구조 선언
queue.append((0, 0))
while queue:

    y, x = queue.popleft()

    visited[y][x] = True

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

        ny = dy + y
        nx = dx + x

        if 0 <= ny < n and 0 <= nx < n:

            # 흰 방인 경우
            if int(nList[ny][nx]) == 1:

                # 방문한 적 없거나 최소 방문인 경우
                if not visited[ny][nx] or minDelBlackRoomList[y][x] < minDelBlackRoomList[ny][nx]:
                    minDelBlackRoomList[ny][nx] = minDelBlackRoomList[y][x]
                    queue.append((ny, nx))

            # 검은 방인 경우
            elif int(nList[ny][nx]) == 0:

                # 방문한 적 없거나 최소 방문인 경우
                if not visited[ny][nx]:
                    minDelBlackRoomList[ny][nx] = minDelBlackRoomList[y][x] + 1
                    queue.append((ny, nx))

                # 방문한 경우
                else:
                    if minDelBlackRoomList[y][x] + 1 < minDelBlackRoomList[ny][nx]:
                        minDelBlackRoomList[ny][nx] = minDelBlackRoomList[y][x] + 1
                        queue.append((ny, nx))

            visited[ny][nx] = True

print(minDelBlackRoomList[n-1][n-1])
