import sys
import math

n, m = map(int, sys.stdin.readline().split())

# 각 우주신의 좌표 저장
god_list = [None]  # 1-index 사용
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    god_list.append((x, y))

# 이미 연결된 통로 정보
parent = [i for i in range(n + 1)]


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa


# 기존 연결들 먼저 union 처리
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

# 가능한 모든 통로 저장
edge_list = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        x1, y1 = god_list[i]
        x2, y2 = god_list[j]

        dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        edge_list.append((dist, i, j))

# 거리 기준으로 정렬 후 MST 구성
edge_list.sort()

cost_sum = 0.0
for dist, a, b in edge_list:
    if find(a) != find(b):
        union(a, b)
        cost_sum += dist

print(f"{cost_sum:.2f}")
