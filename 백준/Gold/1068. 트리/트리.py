import sys

# 몇개의 노드가 있었는지 node_num 에 저장한다
node_num = int(sys.stdin.readline())

# 노드 사이의 관계를 node_tree 리스트에 정의 한다
node_tree = list(map(int, sys.stdin.readline().split()))

# 삭제할 노드 의 인덱스 값을 del_list 에 저장한다
del_indexlist = []
del_indexlist.append(int(sys.stdin.readline()))

# del_list가 완전하게 비게 될때 까지 무한 반복한다.
while(del_indexlist != []):
    # del_list에 있는 첫번째 인데스 가지고온다
    del_value = del_indexlist[0]

    # 현재 비교하고자 하는 값을 node_tree 에서 -2로 변경한다.
    node_tree[del_value] = -2

    # 노드트리에 있는 값중에 현재 비교값을 부모로 두는 자식을 모두 찾고 이 인덱스를 다시 list에 저장한다.
    for count in range(node_num):
        if node_tree[count] == del_value:
            del_indexlist.append(count)

    # del_indexlist에 있는 첫번재 값에 대한 모든 처리가 끝났으므로 list에서 제거한다.
    del del_indexlist[0]

# 리프노드의 개수가 몇개인지 저장하는 변수
leaf_count = 0

for count in range(node_num):
    if node_tree[count] != -2 and count not in node_tree:
        leaf_count += 1

print(leaf_count)