import sys

n = int(sys.stdin.readline().strip())

number_list = list(map(int, sys.stdin.readline().split()))

sort_number_list = list(set(number_list))
sort_number_list.sort()

# index_list = []
# for number in number_list:
#     index_list.append(str(sort_number_list.index(number)))
# print(" ".join(index_list))

index_dic = {}
counter = 0
for number in sort_number_list:
    index_dic[number] = counter
    counter += 1

index_list = []
for number in number_list:
    index_list.append(str(index_dic[number]))

print(" ".join(index_list))