import sys

n, m = map(int, sys.stdin.readline().split())

def PrintAswer(n_list ,n , m, cnt):

    if cnt == m:
        print(*n_list)
        return

    for i in range(n):
        if n_list[cnt - 1] <= i + 1:
            PrintAswer(n_list + [i + 1], n, m, cnt + 1)



cnt = 0
for i in range(n):
    PrintAswer([i + 1], n, m, cnt + 1)