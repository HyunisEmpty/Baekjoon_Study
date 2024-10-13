import sys

n = int(sys.stdin.readline())

if n == 1:
    print(0)
else:
    candidate_1 = int(sys.stdin.readline().strip())
    n_list = [int(sys.stdin.readline().strip()) for _ in range(n - 1)]
    n_list.sort(reverse=True)
    cnt = 0

    while candidate_1 <= n_list[0]:
        cnt += 1
        candidate_1 += 1
        n_list[0] -= 1
        n_list.sort(reverse=True)

    print(cnt)