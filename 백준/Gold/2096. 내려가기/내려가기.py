import sys

n = int(sys.stdin.readline().strip())

dp_list_max = []
dp_list_min = []

for i in range(n):

    dp0, dp1, dp2 = map(int, sys.stdin.readline().strip().split())

    if i == 0:
        dp_list_max = [dp0, dp1, dp2]
        dp_list_min = [dp0, dp1, dp2]
    else:
        max0 = dp0 + max(dp_list_max[0], dp_list_max[1])
        max1 = dp1 + max(dp_list_max[0], dp_list_max[1], dp_list_max[2])
        max2 = dp2 + max(dp_list_max[1], dp_list_max[2])
        dp_list_max[0] = max0
        dp_list_max[1] = max1
        dp_list_max[2] = max2

        min0 = dp0 + min(dp_list_min[0], dp_list_min[1])
        min1 = dp1 + min(dp_list_min[0], dp_list_min[1], dp_list_min[2])
        min2 = dp2 + min(dp_list_min[1], dp_list_min[2])
        dp_list_min[0] = min0
        dp_list_min[1] = min1
        dp_list_min[2] = min2

print(max(dp_list_max), min(dp_list_min))