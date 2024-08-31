import sys

n = int(sys.stdin.readline().strip())
tree_list = []

# 트리 구조를 2중 리스트에 추가
for i in range(n):
    tree_list.append(list(map(int, sys.stdin.readline().strip().split())))

# 트리 구조 아래에서 부터 위로 값을 더하는 for 문
for lev in range(n):

    # 아래층 인덱스 부터 접근
    level = n - 1 - lev
    # print(tree_list[level])

    for i in range(len(tree_list[level]) - 1):

        if tree_list[level][i] >= tree_list[level][i + 1]:
            tree_list[level - 1][i] += tree_list[level][i]
        else:
            tree_list[level - 1][i] += tree_list[level][i + 1]

print(tree_list[0][0])