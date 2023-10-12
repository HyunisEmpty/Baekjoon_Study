import sys

N, target = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
start = end = answer = 0
n_sum = n_list[start]

while end != N:

    if n_sum < target:
        end += 1
        if end != N:
            n_sum += n_list[end]
    else:

        if answer != 0:
            if answer > end - start + 1:
                answer = end - start + 1
        else:
            answer = end - start + 1

        if start == end:
            end += 1
            if end != N:
                n_sum += n_list[end]
        n_sum -= n_list[start]
        start += 1

print(answer)