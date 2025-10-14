import sys
sys.setrecursionlimit(100000)

def quick_sort(arr, p, r):  # l : 첫번재 원소 인덱스, r : 마지막 원소 인덱스

    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)

def partition(arr, p, r):

    global cnt, a, b

    x = arr[r]
    i = p - 1

    for j in range(p, r):

        if arr[j] <= x:
            i += 1
            cnt += 1
            if cnt == K:
                a, b = arr[i], arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    if i + 1 != r:
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        cnt += 1
        if cnt == K:
            a, b = arr[i + 1], arr[r]

    return i + 1

if __name__ == '__main__':

    N, K = map(int, sys.stdin.readline().split())
    N_list = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    a = -1
    b = -1
    quick_sort(N_list, 0, N - 1)

    if a == -1 and b == -1:
        print(-1)
    else:
        if a < b:
            print(a, b)
        else:
            print(b, a)
