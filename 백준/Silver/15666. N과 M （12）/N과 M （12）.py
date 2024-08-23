import sys

n, m = map(int, sys.stdin.readline().split())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0
answer_set = set()

def PrintAnswer(i_list, n, m, index):

    global answer_set
    answer = ' '.join(map(str, i_list))

    # N개의 자연수 중에서 M개를 고른 수열
    if len(i_list) == m:
        # 중복되는 수열을 여러 번 출력하면 안된다.
        if answer not in answer_set:
            answer_set.add(answer)
            print(*i_list)
        return

    # 같은 수를 여러 번 골라도 된다.
    for i in range(index, n):
        PrintAnswer(i_list + [n_list[i]], n, m, i)

PrintAnswer([], n, m, 0)