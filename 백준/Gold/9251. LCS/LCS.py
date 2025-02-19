import sys

str1 = " " + sys.stdin.readline().strip()
str2 = " " + sys.stdin.readline().strip()
n, m = len(str1) - 1, len(str2) - 1
dp = [[0]*(m + 1) for _ in range(n + 1)]
# 왔던 길을 돌아가는 LCS 문자
backTrack = [[0]*(m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            backTrack[i][j] = 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[n][m])

