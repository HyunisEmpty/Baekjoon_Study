import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())

# 각 아이가 가진 사탕 수
candy_list = [0] + list(map(int, sys.stdin.readline().split()))

# 친구 관계 그래프
friend_list = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friend_list[a].append(b)
    friend_list[b].append(a)

# 방문 배열
visited = [False] * (n + 1)

# 그룹별 정보 저장 (group_size: 그룹 인원 수, group_candy: 그룹 총 사탕 수)
group_info = []


def bfs(start):
    """
    친구 관계 기반으로 연결된 모든 아이들을 하나의 그룹으로 묶는 BFS.
    그룹의 인원수와, 그 그룹이 보유한 전체 사탕 개수를 반환한다.
    """
    queue = deque()
    queue.append(start)
    visited[start] = True

    group_size = 1
    group_candy = candy_list[start]

    while queue:
        x = queue.popleft()

        for nxt in friend_list[x]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
                group_size += 1
                group_candy += candy_list[nxt]

    return group_size, group_candy


# 모든 그룹 탐색
for i in range(1, n + 1):
    if not visited[i]:
        size, candy = bfs(i)
        group_info.append((size, candy))

# DP 준비 (k명 이하로 선택 가능)
dp = [0] * (k)

# 배낭 문제 (그룹의 인원수를 무게, 그룹의 사탕 총합을 가치)
for size, candy in group_info:
    for current in range(k - 1, size - 1, -1):
        dp[current] = max(dp[current], dp[current - size] + candy)

print(dp[k - 1])
