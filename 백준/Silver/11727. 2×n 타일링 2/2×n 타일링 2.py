import sys

n = int(sys.stdin.readline().strip())
n_list = [0 for i in range(n + 1)]
n_list[0] = 1   # 문제에서는 존재하지 않는 타일 연산을 위해 존재

# 타일을 채우는 모든 경우 연산
for i in range(n):  # n-1번째 타일 까지만 연산을 진행

    # 3가지의 경우의 수가 발생함
    n_list[i + 1] += (n_list[i] * 1)
    if i + 2 <= len(n_list) - 1:
        n_list[i + 2] += (n_list[i] * 2)
print(n_list[-1] % 10007)
