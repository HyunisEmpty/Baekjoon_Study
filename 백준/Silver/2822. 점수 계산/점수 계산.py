import sys

number_list = []
unsort_list = []
index_list = []
for count in range(8):
    n = int(sys.stdin.readline().strip())
    number_list.append(n)
    unsort_list.append(n)

# 선택 정렬
for i in range(7):
    min_index = i
    for j in range(i, 8):
        if number_list[j] < number_list[min_index]:
            min_index = j
    number_list[i], number_list[min_index] = number_list[min_index], number_list[i]

number_list = number_list[0:3]

for target in number_list:
    for count in range(8):
        if target == unsort_list[count]:
            unsort_list[count] = -1

all_sum = 0
for count in range(8):
    if unsort_list[count] != -1:
        all_sum += unsort_list[count]
        index_list.append(count+1)

print(all_sum)
print(" ".join(str(x) for x in index_list))

