import sys


n, m = map(int, sys.stdin.readline().split())
tree_dic = {}
step = [0 for _ in range(n + 1)]
counter = [0 for _ in range(n + 1)]

# 노드 사이의 관계를 담을 딕셔너리
for i in range(n):
    tree_dic[i + 1] = []

# 관계의 수(m)만큼 서로의 키에 값으로 서로를 추가 
for i in range(m):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    tree_dic[node_1].append(node_2)
    tree_dic[node_2].append(node_1)

for i in range(n):

    # 큐와 접근 확인을 위한 셋의 초기값으로 모든 노드가 한번씩 온다.
    bfs_queue = [i + 1]
    bfs_set = {i + 1}
    step[i + 1] = 1
    count = 0

    # BFS 알고리즘 
    while len(bfs_queue) != 0:

        node = bfs_queue.pop(0)

        for contact_node in tree_dic[node]:
            if contact_node not in bfs_set:
                bfs_set.add(contact_node)
                bfs_queue.append(contact_node)
                # 현재 접근한 노드가 루트 노드로 부터 몇번째 층에 있는지를 저장 
                count += step[node]
                # 접근한 노드의 다음노드의 레벨을 현재노드를 인덱스 값으로 하는 리스트의 값으로 저장 
                step[contact_node] = step[node] + 1

    counter[i + 1] = count

# 최솟값을 구하는 for문, 최솟값이 중복이면 인덱스가 작은 것을 저장
min_val = -1
min_index = 0
for i in range(1, n + 1):
    if min_val == -1:
        min_val = counter[i]
        min_index = i
    else:
        if min_val > counter[i]:
            min_val = counter[i]
            min_index = i

print(min_index)