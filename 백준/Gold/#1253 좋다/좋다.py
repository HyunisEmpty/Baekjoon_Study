import sys

n = int(sys.stdin.readline().strip())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
answer = 0

for i in range(n):

    left = 0
    right = n - 1

    while left < right:

        if left != i and right != i:
            if n_list[left] + n_list[right] == n_list[i]:
                answer += 1
                break
            elif n_list[left] + n_list[right] < n_list[i]:
                left += 1
            else:
                right -= 1
        else:
            if left == i:
                left += 1
            else:
                right -= 1

print(answer)