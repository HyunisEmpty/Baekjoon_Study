import sys

# 퀵 정렬 함수
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


n = int(sys.stdin.readline().strip())

number_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

number_list = quick_sort(number_list)

for number in number_list:
    print(number)