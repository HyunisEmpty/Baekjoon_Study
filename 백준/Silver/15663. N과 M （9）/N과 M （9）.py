import sys

n, m = map(int, sys.stdin.readline().split())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0
answer_set = set()

def PrintAnswer(i_list, i_set, n, m):

    global answer_set
    answer = ' '.join(map(str, i_list))

    if len(i_list) == m:
        if answer not in answer_set:
            answer_set.add(answer)
            print(*i_list)
        return

    for i in range(n):
        if i not in i_set:
            new_set = i_set.copy()
            new_set.add(i)
            PrintAnswer(i_list + [n_list[i]], new_set,n, m)

PrintAnswer([], set(), n, m)