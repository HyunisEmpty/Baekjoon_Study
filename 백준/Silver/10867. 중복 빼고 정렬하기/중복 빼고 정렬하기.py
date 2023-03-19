import sys

n = int(sys.stdin.readline().strip())
unset_number_list = list(map(int, sys.stdin.readline().split()))
number_list = list(set(unset_number_list))

for i in range(len(number_list)-1):
    min_index = i
    for j in range(i, len(number_list)):
        if number_list[j] < number_list[min_index]:
            min_index = j
    number_list[i], number_list[min_index] = number_list[min_index], number_list[i]
print(" ".join(str(x) for x in number_list))