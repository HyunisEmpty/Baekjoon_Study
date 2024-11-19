import sys

n, m, k = map(int, sys.stdin.readline().split())
n_list = [i for i in range(n+1)]      # 루트 노드(친구)를 저장 하는 리스트
fee_list = [0] + list(map(int, sys.stdin.readline().split()))   # 사람별 요구하는 친구비를 저장하는 리스트


def FindRootNode(node):

    global n_list

    if node != n_list[node]:    # 부모가 루트 노드가 아닌 경우
        n_list[node] = FindRootNode(n_list[node])

    return n_list[node]


# m개의 친구 관계 정의
for _ in range(m):

    friend1, friend2 = map(int, sys.stdin.readline().split())

    root1 = FindRootNode(friend1)
    root2 = FindRootNode(friend2)

    # 서로 같은 친구 관계에 속하지 않는 경우
    if root1 != root2:
        if fee_list[root1] < fee_list[root2]:   # root1이 친구비가 더 적은 경우 root2의 부모가 된다.
            n_list[root2] = root1
        else:
            n_list[root1] = root2

total_fee = 0
for i in range(len(n_list)):

    if n_list[i] == i:
        total_fee += fee_list[i]

if total_fee > k:
    print("Oh no")
else:
    print(total_fee)