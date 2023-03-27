import sys


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


college_w = []
college_k = []
for i in range(20):
    if i < 10:
        college_w.append(int(sys.stdin.readline().strip()))
    else:
        college_k.append(int(sys.stdin.readline().strip()))

selection_sort(college_w)
selection_sort(college_k)

print(college_w[9] + college_w[8] + college_w[7], college_k[9] + college_k[8] + college_k[7])