import sys

n = int(sys.stdin.readline().strip())

start = end = 1
n_sum = 1
answer = 0

while end < n + 1:

    if n_sum < n:
        end += 1
        if end < n + 1:
            n_sum += end
    elif n < n_sum:
        n_sum -= start
        start += 1
    else:
        answer += 1
        n_sum -= start
        start += 1

print(answer)