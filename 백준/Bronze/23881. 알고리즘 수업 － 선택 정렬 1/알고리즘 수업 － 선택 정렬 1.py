import sys

N, K = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

def selection_sort(arr):
    n = len(arr)
    cnt = 0
    # 뒤의 원소 부터 접근
    for i in range(n - 1, 0, -1):
        max_index = i
        for j in range(i):
            if arr[max_index] < arr[j]:
                max_index = j

        # swap이 발생 하는 경우
        if max_index != i:
            cnt += 1
            arr[i], arr[max_index] = arr[max_index], arr[i]

        # K번째 발생한 swap 이라면
        if cnt == K:
            if arr[max_index] < arr[i]:
                print(arr[max_index], arr[i])
            else:
                print(arr[i], arr[max_index])
            return

    print(-1)
    return

selection_sort(N_list)