import sys

n = int(sys.stdin.readline().strip())
tree_dic = {}

# 처음에는 누가 부모인지 모름 그렇기에 서로를 서로의 값으로 저장
for i in range(n-1):
    node_x, node_y = map(int, sys.stdin.readline().split())

    if node_x in tree_dic.keys():
        tree_dic[node_x].append(node_y)
    elif node_x not in tree_dic.keys():
        tree_dic[node_x] = [node_y]

    if node_y in tree_dic.keys():
        tree_dic[node_y].append(node_x)
    elif node_y not in tree_dic.keys():
        tree_dic[node_y] = [node_x]

# print(tree_dic)

answer_list = []
for i in range(n-1):
    answer_list.append(0)

# 부모 리스트가 빌때까지 반복하며 1은 루트로 초기값이다.
parent_list = [1]
while len(parent_list) != 0:

    # 값을 입력받은 즉시 삭제
    parent_node = parent_list[0]
    parent_list.remove(parent_node)

    # 부모 노드의 모든 자식에게 접근
    for node in tree_dic[parent_node]:
        # 부모 리스트에 노드 추가
        parent_list.append(node)
        # 키에 대한 값으로 자식 노드만 리스트에 저장해야 하기에 부모 노드를 삭제
        tree_dic[node].remove(parent_node)
        # 정답 출력 리스트에 현재 노드의 부모 노드를 저장
        answer_list[node-2] = parent_node

for i in answer_list:
    print(i)