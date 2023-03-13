# 삽입 정렬
import sys

unsorted_list = [int(sys.stdin.readline().strip()) for _ in range(5)]
sorted_list = [unsorted_list[0]]

for i in range(1, 5):
    for j in range(len(sorted_list)):
        if sorted_list[j] > unsorted_list[i]:
            sorted_list.insert(j, unsorted_list[i])
            break
        if j == len(sorted_list)-1:
            sorted_list.insert(j+1, unsorted_list[i])

ave = 0
for count in range(5):
    ave += sorted_list[count]

print(int(ave/5))
print(sorted_list[2])
