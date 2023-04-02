import sys

number_list = []

for i in range(9):
    number_list.append(int(sys.stdin.readline().strip()))

max_num = -1
max_index = -1
for i in range(9):
    if number_list[i] > max_num:
        max_num = number_list[i]
        max_index = i + 1

print(max_num)
print(max_index)