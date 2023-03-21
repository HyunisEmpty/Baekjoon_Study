import sys


# y값만 있는 리스트를 병합 정렬
def merge_sort(arr):
    if (len(arr)) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0

    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr


n = int(sys.stdin.readline().strip())

coordinate_dic = {}     # y값을 키로 x를 리스트에 저장하여 값으로 본다.
y_list = []             # y값을 기준으로 정렬하므로 y값을 담을 리스트를 준비한다.

for count in range(n):
    # x 좌표와 y좌표를 입력 받습니다.
    x, y = map(int, sys.stdin.readline().split())

    # y 좌표가 좌표 사전에 들어 있지 않다면
    if y not in coordinate_dic.keys():
        coordinate_dic[y] = [x]
        y_list.append(y)
    else:
        coordinate_dic[y].append(x)

y_list = merge_sort(y_list)

for y_key in y_list:
    coordinate_dic[y_key] = merge_sort(coordinate_dic[y_key])
    for x_val in coordinate_dic[y_key]:
        print(str(x_val) + " " + str(y_key))