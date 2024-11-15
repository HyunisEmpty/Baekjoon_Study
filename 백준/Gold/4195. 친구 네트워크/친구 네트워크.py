import sys

test_case = int(sys.stdin.readline().strip())
network = dict()

def FindRootNode(name):     # 네트워크에서 root node를 찾음
    global network

    if network[name][0] != name:
        network[name][0] = FindRootNode(network[name][0])  # 경로 압축 적용
    return network[name][0]

for test in range(test_case):
    F = int(sys.stdin.readline().strip())
    network.clear()

    for _ in range(F):
        name1, name2 = map(str, sys.stdin.readline().split())

        if name1 not in network:
            network[name1] = [name1, 1]
        if name2 not in network:
            network[name2] = [name2, 1]

        name1_root = FindRootNode(name1)
        name2_root = FindRootNode(name2)

        if name1_root != name2_root:
            # Union by Rank 적용
            if network[name1_root][1] >= network[name2_root][1]:
                network[name2_root][0] = name1_root
                network[name1_root][1] += network[name2_root][1]
            else:
                network[name1_root][0] = name2_root
                network[name2_root][1] += network[name1_root][1]

        print(network[FindRootNode(name1)][1])  # 최종 루트에서 그룹 크기 출력
