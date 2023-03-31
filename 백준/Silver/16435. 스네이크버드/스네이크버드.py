import sys

fruit_number, default_length = map(int, sys.stdin.readline().split())

fruit_list = list(map(int, sys.stdin.readline().split()))

# 선택 정렬
for i in range(fruit_number-1):
    min_index = i
    for j in range(i, fruit_number):
        if fruit_list[min_index] > fruit_list[j]:
            min_index = j
    fruit_list[min_index], fruit_list[i] = fruit_list[i], fruit_list[min_index]


for fruit in fruit_list:
    if default_length >= fruit:
        default_length += 1
    else:
        break

print(default_length)