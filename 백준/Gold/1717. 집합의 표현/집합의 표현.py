import sys

n, m = map(int, sys.stdin.readline().split())
n_list = [i for i in range(n + 1)]


def FindRootNode(node1):

    global n_list

    while n_list[node1] != node1:  # node1이 루트 노드가 아니라면 
        node1 = n_list[node1]     # 현재 노드를 부모 노드로 변경
        
    return node1


for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())

    a_root = FindRootNode(a)
    b_root = FindRootNode(b)

    if command == 0:     # 합집합 연산

        n_list[b_root] = a_root             # b집합을 a집합과 합치고 b의 루트 노드를 a루트의 자식 노드로 변경

        # 경로 압축
        n_list[b] = a_root
        n_list[a] = a_root

    elif command == 1:
        
        if a_root == b_root:
            print("YES")
        else:
            print("NO")