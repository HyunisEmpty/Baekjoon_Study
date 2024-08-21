import sys

n, m = map(int, sys.stdin.readline().split())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0


def PrintAnswer(i_list, i_set, n, m):

    if len(i_list) == m:
        print(*i_list)
        return

    for i in range(n):
        if n_list[i] not in i_set:
            new_set = i_set.copy()
            new_set.add(n_list[i])
            PrintAnswer(i_list + [n_list[i]], new_set,n, m)

PrintAnswer([], set(), n, m)