import sys

N, target = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
answer = start = end = 0

while end != N:

    n_sum = sum(n_list[start:end+1])

    if n_sum == target:
        answer += 1
        if start == end:
            end += 1
        start += 1
    elif n_sum < target:
        end += 1
    elif n_sum > target:
        if start == end:
            end += 1
        start += 1

print(answer)