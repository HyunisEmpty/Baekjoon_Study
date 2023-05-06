import sys

tree_deep = int(sys.stdin.readline().strip())
dfs_node_list = list(map(int, sys.stdin.readline().split()))

tree_level_list = [[] for i in range(tree_deep)]


def DFS(tree_list, level):

    if len(tree_list) == 1:
        tree_level_list[level-1].append(tree_list[0])
        
    else:
        mid_index = len(tree_list)//2
        tree_level_list[level - 1].append(tree_list[mid_index])
        DFS(tree_list[:mid_index], level + 1)
        DFS(tree_list[mid_index+1:], level + 1)



DFS(dfs_node_list, 1)
for i in range(tree_deep):
    print(" ".join([str(x) for x in tree_level_list[i]]))