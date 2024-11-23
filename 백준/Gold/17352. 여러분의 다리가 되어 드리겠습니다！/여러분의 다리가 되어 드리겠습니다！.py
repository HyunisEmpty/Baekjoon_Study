import sys

n = int(sys.stdin.readline().strip())
n_list = [i for i in range(n+1)]


def FindRootNode(node):

    if node != n_list[node]:
        n_list[node] = FindRootNode(n_list[node])

    return n_list[node]


for i in range(n - 2):
    node1, node2 = map(int, sys.stdin.readline().strip().split())

    root1 = FindRootNode(node1)
    root2 = FindRootNode(node2)

    n_list[root2] = root1

answerList = []
for i in range(1, n + 1):

    if n_list[i] == i:
        answerList.append(i)

print(" ".join(map(str, answerList)))

