import sys
import random

node_max, edge_max = map(int, sys.stdin.readline().split())
tree_dic = {}

for i in range(edge_max):
    node_x, node_y = map(int, sys.stdin.readline().split())

    if node_x not in tree_dic:
        tree_dic[node_x] = [node_y]
    else:
        tree_dic[node_x].append(node_y)

    if node_y not in tree_dic:
        tree_dic[node_y] = [node_x]
    else:
        tree_dic[node_y].append(node_x)

# 다른 노드와 연결되어 있지 않은 정점또한 연결 요소 이므로 딕셔너리에 추가해 카운트 하도록 한다.
for i in range(1, node_max - len(tree_dic.keys()) + 1):
    tree_dic[-1 * i] = []

# BFS Algorithm
count = 0
while len(tree_dic.keys()) != 0:

    # 무작위 노드를 받아와 노드와 연결된 모든 노드에 접근한다.
    random_node = random.choice(list(tree_dic.keys()))
    # 접근 했던 노드인지 확인하기 위한 집합
    bfs_set = {random_node}
    bfs_queue = [random_node]

    while len(bfs_queue) != 0:
        node = bfs_queue.pop(0)

        for contact_node in tree_dic[node]:
            if contact_node not in bfs_set:
                bfs_set.add(contact_node)
                bfs_queue.append(contact_node)

        tree_dic.pop(node)

    count += 1

# 모든 노드가 서로에게 연결되어 있지 않은 경우
print(count)