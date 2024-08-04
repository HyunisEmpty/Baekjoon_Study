import sys

n, m = map(int, sys.stdin.readline().split())
n_list = [i for i in range(1, n + 1)]

def nm_function(i_list, index):

    # 임의로 선택한 원소가 m개 이하인 경우
    if len(i_list) < m:
        for i in range(index + 1, n):
            nm_function(i_list + [n_list[i]], i)
    elif len(i_list) == m:
        print(*i_list)

for i in range(n):
    nm_function([i + 1], i)