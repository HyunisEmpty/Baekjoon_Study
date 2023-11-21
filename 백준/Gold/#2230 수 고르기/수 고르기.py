import sys

n, m = map(int, sys.stdin.readline().split())
n_list = []
min_val = 2000000001

for i in range(n):
    n_list.append(int(sys.stdin.readline().strip()))
n_list.sort()

left = right = 0

while right != n:
    changes_val = n_list[right] - n_list[left]

    if changes_val < m:
        right += 1
    elif changes_val > m:
        if changes_val < min_val:
            min_val = changes_val

        left += 1
        if left == right:
            right += 1
    else:
        min_val = m
        break

print(min_val)

