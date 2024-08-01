import sys

n = int(sys.stdin.readline().strip())
n_list = [0] + list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())

for i in range(1, n + 1):
    n_list[i] += n_list[i - 1]

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())

    print(n_list[b] - n_list[a - 1])