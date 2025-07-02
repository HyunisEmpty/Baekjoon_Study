import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().split()))
cnt_list = [1] * n

for i in range(n):
   for j in range(i + 1, n):
      if n_list[i] < n_list[j] and cnt_list[i] + 1 > cnt_list[j]:
         cnt_list[j] = cnt_list[i] + 1

print(max(cnt_list))
