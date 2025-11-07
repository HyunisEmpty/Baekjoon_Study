import sys

n = int(sys.stdin.readline().strip())
dp = [[] for _ in range(n + 1)]

dp[1] += [1]
for i in range(2, n + 1):

    # 직전 i에 1 증가한 경우
    dp[i] = dp[i - 1] + [i]
    if i % 2 == 0 and len(dp[i]) > len(dp[i//2]) + 1:  # i가 2로 나누어 떨어지는 경우
        dp[i] = dp[i//2] + [i]
    if i % 3 == 0 and len(dp[i]) > len(dp[i//3]) + 1:  # i가 3으로 나누어 떨어지는 경우
        dp[i] = dp[i//3] + [i]

print(len(dp[n]) -1)
print(*dp[n][::-1])