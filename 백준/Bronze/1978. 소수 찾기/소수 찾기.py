import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().split()))

answer = 0
for number in n_list:
    count = 0
    for i in range(1 , number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        answer += 1

print(answer)