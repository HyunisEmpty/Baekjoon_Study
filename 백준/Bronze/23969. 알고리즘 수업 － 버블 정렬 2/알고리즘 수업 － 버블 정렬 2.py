import sys

def BubbleSort():

    global N_list
    cnt = 0

    for i in range(len(N_list)-1, 0 , -1):
        for j in range(i):
            if N_list[j] > N_list[j + 1]:
                N_list[j], N_list[j + 1] = N_list[j + 1], N_list[j]
                cnt += 1

                if cnt == K:
                    print(" ".join(map(str, N_list)))
                    return

    print(-1)
    return

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    N_list = list(map(int, sys.stdin.readline().split()))

    BubbleSort()
