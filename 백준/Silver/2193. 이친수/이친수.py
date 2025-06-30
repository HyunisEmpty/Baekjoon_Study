import sys

n = int(sys.stdin.readline().strip())

dp0 = [0] * 91
dp1 = [0] * 91

dp1[1] = 1
dp0[2] = 1
for i in range(3, n + 1):
   dp0[i] = dp0[i - 1] + dp1[i - 1]
   dp1[i] = dp0[i - 1]

print(dp0[n] + dp1[n])