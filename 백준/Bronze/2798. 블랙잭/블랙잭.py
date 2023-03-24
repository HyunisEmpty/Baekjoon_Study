import sys

n, m = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))
sum_ijk = 0
number_max = 0

# 브루트 포스 알고리즘
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != k and i != j and j != k:
                sum_ijk = 0
                sum_ijk = number_list[i] + number_list[j] + number_list[k]
                if number_max < sum_ijk <= m:
                    number_max = sum_ijk

print(number_max)