# 삽입 정렬
import sys

n = int(sys.stdin.readline().strip())

unsorted_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
sorted_list = [unsorted_list[0]]

for i in range(1, n):
    for j in range(len(sorted_list)):
        if sorted_list[j] > unsorted_list[i]:
            sorted_list.insert(j, unsorted_list[i])
            break
        if j == len(sorted_list)-1:
            sorted_list.insert(j+1, unsorted_list[i])

for count in range(n):
    print(sorted_list[count])
