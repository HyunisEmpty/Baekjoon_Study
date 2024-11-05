import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
n_list = [[] for _ in range(n + 1)]

for _ in range(m):  # 컴퓨터 사이의 신뢰 관계 리스트에 정리
    trust_computer, trusted_computer = map(int, sys.stdin.readline().split())
    n_list[trusted_computer].append(trust_computer)

queue = deque()
max_cnt = 0
max_list = []
for i in range(1, n + 1):
    n_visited = [False for _ in range(n + 1)]
    if len(n_list[i]) > 0:  # 자신을 신뢰하는 컴퓨터가 있을때만 연산

        queue.append(i)
        n_visited[i] = True

        cnt = 0
        while queue:

            computer = queue.popleft()
            cnt += 1

            for trust_computer in n_list[computer]:
                if not n_visited[trust_computer]:
                    queue.append(trust_computer)
                    n_visited[trust_computer] = True

        if cnt > max_cnt:
            max_cnt = cnt
            max_list = [i]
        elif cnt == max_cnt:
            max_list.append(i)

max_list.sort()
print(*max_list)

