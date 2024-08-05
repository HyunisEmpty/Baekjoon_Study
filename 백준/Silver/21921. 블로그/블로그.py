import sys

n, x = map(int, sys.stdin.readline().split())
sum_list = [0] + list(map(int, sys.stdin.readline().split()))

max_visitant = 0
max_day = 0
start = 0
end = x

for i in range(1, n + 1):
    sum_list[i] += sum_list[i - 1]

while end < len(sum_list):

    if max_visitant < sum_list[end] - sum_list[start]:
        max_visitant = sum_list[end] - sum_list[start]
        max_day = 1
    elif max_visitant == sum_list[end] - sum_list[start]:
        max_day += 1

    start += 1
    end += 1

if max_visitant == 0:
    print("SAD")
else:
    print(max_visitant)
    print(max_day)