import sys

n, m = map(int, sys.stdin.readline().split())
n_list = [i for i in range(n + 1)]

for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())

    if command == 0:     # 합집합 연산

        a_root = a
        b_root = b

        while n_list[a_root] != a_root:   # a에는 root 노드가 저장됨
            a_root = n_list[a_root]

        while n_list[b_root] != b_root:   # b에는 root 노드가 저장됨
            b_root = n_list[b_root]

        # 경로 압축
        n_list[b_root] = a_root
        n_list[b] = a_root
        n_list[a] = a_root

    elif command == 1:

        a_root = a
        b_root = b

        while n_list[a_root] != a_root:  # a에는 root 노드가 저장됨
            a_root = n_list[a_root]

        while n_list[b_root] != b_root:  # b에는 root 노드가 저장됨
            b_root = n_list[b_root]

        if a_root == b_root:
            print("YES")
        else:
            print("NO")