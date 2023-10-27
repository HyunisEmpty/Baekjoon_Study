import sys

n = int(sys.stdin.readline().strip())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline().strip())

answer = 0
right = 0
left = len(n_list) - 1

while right < left:

    rl = n_list[right] + n_list[left]

    if rl == x:
        answer += 1
        right += 1
    elif rl < x:
        right += 1
    else:
        left -= 1

print(answer)
