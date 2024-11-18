import sys

n, m = map(int, sys.stdin.readline().split())
n_list = [i for i in range(n)]      # 노드별 루트 노드를 저장
rank_list = [0 for i in range(n)]   # 트리의 높이를 저장


def FindRootNode(node):

    global n_list

    if node != n_list[node]:
        n_list[node] = FindRootNode(n_list[node])

    return n_list[node]

flag = False
for i in range(m):

    node1, node2 = map(int, sys.stdin.readline().split())
    root1 = FindRootNode(node1)     # node1의 루트 노드
    root2 = FindRootNode(node2)     # noed2의 루트 노드

    if node1 != node2: # 서로 다른 노드 일때, 두 루트 노드가 같다면
        if root1 == root2:  # 서로 같은 집합에서 서로를 연결
            flag = True
            break

    # Rank Union
    if root1 != root2:
        if rank_list[root1] > rank_list[root2]:     # root1의 트리 깊이가 더 깊은 경우
            n_list[root2] = root1
        elif rank_list[root1] < rank_list[root2]:   # root2의 트리 깊이가 더 깊은 경우
            n_list[root1] = root2
        else:
            n_list[root2] = root1
            rank_list[root1] += 1

if flag:
    print(i + 1)
else:
    print(0)