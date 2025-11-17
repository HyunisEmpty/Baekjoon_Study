import sys

n = int(sys.stdin.readline())

# 각 좌표를 저장
planet_list = []
for idx in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    planet_list.append((idx, x, y, z))

# 모든 간선을 만들지 않고, x/y/z별로 정렬 후 인접 행성끼리만 간선 생성
edge_list = []

# X 기준 정렬
planet_list.sort(key=lambda x: x[1])
for i in range(n - 1):
    a = planet_list[i]
    b = planet_list[i + 1]
    edge_list.append((abs(a[1] - b[1]), a[0], b[0]))

# Y 기준 정렬
planet_list.sort(key=lambda x: x[2])
for i in range(n - 1):
    a = planet_list[i]
    b = planet_list[i + 1]
    edge_list.append((abs(a[2] - b[2]), a[0], b[0]))

# Z 기준 정렬
planet_list.sort(key=lambda x: x[3])
for i in range(n - 1):
    a = planet_list[i]
    b = planet_list[i + 1]
    edge_list.append((abs(a[3] - b[3]), a[0], b[0]))

# 비용 기준으로 간선을 정렬 (Kruskal)
edge_list.sort()

# 유니온 파인드 준비
parent = [i for i in range(n)]


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


# MST 구성
cost_sum = 0
for cost, a, b in edge_list:
    if find(a) != find(b):
        union(a, b)
        cost_sum += cost

print(cost_sum)
