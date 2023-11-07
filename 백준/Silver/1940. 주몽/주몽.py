import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
left = answer = 0
right = n - 1

while left < right:
    if n_list[left] + n_list[right] == m:
        answer += 1
        left += 1
    elif n_list[left] + n_list[right] > m:
        right -= 1
    else:
        left += 1

print(answer)