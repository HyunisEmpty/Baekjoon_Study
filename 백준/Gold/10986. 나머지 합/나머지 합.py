import sys

n, m = map(int, sys.stdin.readline().split())
n_list = [0] + list(map(int, sys.stdin.readline().split()))
remain_list = [0 for _ in range(m)]
answer = 0

for i in range(1, n + 1):
    n_list[i] = n_list[i] + n_list[i - 1]

for i in range(1, n + 1):
    n_list[i] = n_list[i] % m
    remain_list[n_list[i]] += 1
    
answer = remain_list[0]

for i in range(m):
    answer += remain_list[i] * (remain_list[i] - 1) // 2

print(answer)