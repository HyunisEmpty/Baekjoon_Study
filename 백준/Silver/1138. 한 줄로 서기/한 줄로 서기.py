import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))   # 자신보다 큰 사람의 수를 저장
answer_list = [0 for _ in range(n)]

for i in range(n):      # n_list 접근

    cnt = 0

    for j in range(n):  # answer_list 접근

        if cnt == n_list[i] and answer_list[j] == 0:
            answer_list[j] = i + 1
            break

        if answer_list[j] == 0:
            cnt += 1

print(*answer_list)