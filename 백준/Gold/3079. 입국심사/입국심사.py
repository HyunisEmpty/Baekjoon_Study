import sys

n, m = map(int, sys.stdin.readline().split())
n_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

left = 1
right = max(n_list) * m # 가장 오래 걸리는 심사대에 모두 줄을 선 경우
min_time = 0

while left <= right:

    passed_people = 0
    mid = (left + right) // 2

    for table_time in n_list:
        passed_people += mid//table_time

    if passed_people >= m:
        min_time = mid
        right = mid - 1
    else:
        left = mid + 1

print(min_time)