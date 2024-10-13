import sys

n = int(sys.stdin.readline().strip())
n_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
n_list.sort(reverse=True)
flag = False

for i in range(2, len(n_list)):

    if n_list[i - 2] < n_list[i-1] + n_list[i]:
        flag = True
        print(n_list[i] + n_list[i-1] + n_list[i-2])
        break
    else:
        flag = False

if not flag:
    print(-1)
    