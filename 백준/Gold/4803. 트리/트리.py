import sys

cnt = 1


# 루트 노드 출력
def FindRootNode(node):
    global parent

    if node != parent[node]:
        parent[node] = FindRootNode(parent[node])

    return parent[node]


# 두 노드 병합
def Union(root1, root2):

    global parent


    if root1 != root2 and (root1 != 0 and root2 != 0):  # 서로 다른 부분 집합인 경우
        parent[root1] = root2
    else:
        # 0은 실제로 존재 하지 않는 노드
        parent[root2] = 0
        parent[root1] = 0


while True:

    n, m = map(int, sys.stdin.readline().split())

    if n == m == 0:     # 입력의 마지막 줄에는 0이 두 개 주어진다.
        break

    parent = [i for i in range(n + 1)]

    for _ in range(m):
        node1, node2 = map(int, sys.stdin.readline().split())

        # node1과 node2 병합
        Union(FindRootNode(node1), FindRootNode(node2))

    tree_cnt = 0
    for i in range(1, len(parent)):
        if i == parent[i]:
            tree_cnt += 1

    if tree_cnt == 0:
        print(f"Case {cnt}: No trees.")
    elif tree_cnt == 1:
        print(f"Case {cnt}: There is one tree.")
    else:
        print(f"Case {cnt}: A forest of {tree_cnt} trees.")

    cnt += 1