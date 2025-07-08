import sys

N, S, M = map(int, sys.stdin.readline().split())
v_list = list(map(int, sys.stdin.readline().split()))

n_list = [-1] * (M + 1)
n2_list = [-1] * (M + 1)
n_list[S] = 0 # 각각의 볼륨이 최대 몇번째 곡에서 실행되었는지 저장.

for i in range(N):  # N개의 곡에 대해서 연산을 수행
    now_volume = v_list[i]

    for j in range(len(n_list)):    # n_list
        if n_list[j] == i:
            if 0 <= j + now_volume <= M:
                n2_list[j + now_volume] = i + 1
            if 0 <= j - now_volume <= M:
                n2_list[j - now_volume] = i + 1

    for j in range(len(n2_list)):
        n_list[j] = n2_list[j]

max_index = -1
for i in range(len(n_list)):
    if n_list[i] == N:
        max_index = i

if max_index == -1:
    print(-1)
else:
    print(max_index)