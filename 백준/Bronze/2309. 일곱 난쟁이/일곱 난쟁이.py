import sys

number_list = [int(sys.stdin.readline().strip()) for _ in range(9)]

# 삽입 정렬
for i in range(8):
    min_index = i
    for j in range(i, 9):
        if number_list[min_index] > number_list[j]:
            min_index = j

    number_list[min_index], number_list[i] = number_list[i], number_list[min_index]


all_sum = 0
height_sum = 0
for i in range(9):
    all_sum += number_list[i]

# 브루트포스 알고리즘
flag = False
for i in range(9):
    for j in range(9):
        height_sum = all_sum
        if i != j:
            height_sum -= number_list[i]
            height_sum -= number_list[j]
            if height_sum == 100:
                flag = True
                number_list[i] = -1
                number_list[j] = -1
                break
    if flag:
        break

for i in range(9):
    if number_list[i] > 0:
        print(number_list[i])


