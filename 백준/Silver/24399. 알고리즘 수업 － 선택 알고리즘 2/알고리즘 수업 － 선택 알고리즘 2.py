import sys
sys.setrecursionlimit(100000)

def select(arr, p, r, q):   # p는 인덱스 0번째 원소, r은 마지막 원소 인덱스, q번째 작은 원소

    if p == r:
        return arr[p]

    t = partition(arr, p, r)
    k = t - p + 1
    if q < k:
        return select(arr, p, t - 1, q)
    elif q == k:
        return arr[t]
    else:
        return select(arr, t + 1, r, q - k)

def partition(arr, p, r):

    global cnt, answer

    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            cnt += 1
            if cnt == K:
                answer = arr[:]
    if i + 1 != r:
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        cnt += 1
        if cnt == K:
            answer = arr[:]
    return i + 1

if __name__ == '__main__':

    N, Q, K = map(int, sys.stdin.readline().split())
    N_list = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    answer = []
    select(N_list, 0, N - 1, Q)

    if len(answer) == 0:
        print(-1)
    else:
        print(" ".join(map(str, answer)))