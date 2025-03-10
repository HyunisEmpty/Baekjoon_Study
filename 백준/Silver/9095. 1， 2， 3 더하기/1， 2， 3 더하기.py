import sys

test_case = int(sys.stdin.readline())

for test in range(test_case):

    dp = [0 for _ in range(12)]

    for i in range(1, 4):
        dp[i] = 1

    n = int(sys.stdin.readline().strip())

    for i in range(1, n + 1):

        if i == 1:
            dp[i] = dp[i]
        elif i == 2:
            dp[i] = dp[i] + dp[i - 1]
        elif i == 3:
            dp[i] = dp[i] + dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i] + dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])

