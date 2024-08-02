import sys

n = int(sys.stdin.readline().strip())
sum_list = [0] + list(map(int, sys.stdin.readline().strip().split()))
answer = 0

# 누적합 연산
for i in range(1, n + 1):
    sum_list[i] += sum_list[i - 1]

for i in range(1, n + 1):
    answer += (sum_list[i] - sum_list[i - 1]) * (sum_list[n] - sum_list[i])

print(answer)