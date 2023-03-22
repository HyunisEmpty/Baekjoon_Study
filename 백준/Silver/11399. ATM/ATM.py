import sys

t = int(sys.stdin.readline().strip())

time_list = list(map(int, sys.stdin.readline().split()))

# 선택 정렬
for i in range(t-1):
    min_index = i
    for j in range(i, t):
        if time_list[min_index] > time_list[j]:
            min_index = j

    time_list[min_index], time_list[i] = time_list[i], time_list[min_index]

time_index = 0
all_sum = 0
for count in range(t, 0, -1):
    all_sum += time_list[time_index] * count
    time_index += 1

print(all_sum)