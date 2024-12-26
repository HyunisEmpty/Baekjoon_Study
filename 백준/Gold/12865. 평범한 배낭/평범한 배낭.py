import sys

n, k = map(int, sys.stdin.readline().split())

weight = [0 for _ in range(n + 1)]
value = [0 for _ in range(n + 1)]
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n):

    weight[i], value[i] =map(int, sys.stdin.readline().split())

for i in range(n + 1):  # 현재 물건에 접근

    for j in range(k + 1):  # 각 무게에 접근

        if j - weight[i] >= 0:      # 물건을 추가 가능한 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
        else:                   # 물건 추가가 불가능한 경우
            dp[i][j] = dp[i-1][j]

# for _ in range(n):
#     print(dp[_])

print(max(dp[n-1]))