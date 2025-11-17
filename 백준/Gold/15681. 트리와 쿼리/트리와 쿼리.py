import sys
# 재귀를 사용하지 않으므로 recursionlimit 조정 불필요
input = sys.stdin.readline

# 트리의 노드 개수 n, 루트 r, 쿼리 개수 q 입력
n, r, q = map(int, input().split())

# 트리의 연결 관계를 저장할 리스트
tree_list = [[] for _ in range(n + 1)]

# 트리 간선 입력
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree_list[a].append(b)
    tree_list[b].append(a)

# 각 노드를 루트 기준으로 방문할 순서를 얻기 위한 스택(반복 DFS)
parent = [-1] * (n + 1)   # 부모 정보 저장 (방문 체크 대체)
order = []                # 전위 방문 순서를 저장 (나중에 역순으로 처리)

stack = [r]
parent[r] = 0             # 루트의 부모는 0(없는 것으로 표시)

# 반복 DFS로 방문 순서(전위)를 얻음
while stack:
    node = stack.pop()
    order.append(node)
    # 인접 노드 중 부모가 아닌 노드를 스택에 추가
    for nxt in tree_list[node]:
        if parent[nxt] == -1:
            parent[nxt] = node
            stack.append(nxt)

# 이제 order의 역순으로 서브트리 크기를 계산 (후위 처럼 동작)
subtree_size = [0] * (n + 1)
for node in reversed(order):
    # 자기 자신 포함
    subtree_size[node] = 1
    # 자식들의 subtree_size 합산
    for nxt in tree_list[node]:
        if parent[nxt] == node:   # nxt가 node의 자식이면 더해준다
            subtree_size[node] += subtree_size[nxt]

# q개의 쿼리 처리
for _ in range(q):
    target = int(input())
    print(subtree_size[target])
