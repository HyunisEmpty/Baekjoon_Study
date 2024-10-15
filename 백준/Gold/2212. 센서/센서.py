import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().strip().split()))
n_list.sort()

panel_list = []     # 모든 센서 사이의 구간 길이 저장
for i in range(1, n):
    panel_list.append(n_list[i] - n_list[i - 1])
panel_list.sort(reverse=True)

answer = n_list[-1] - n_list[0]     # 센서가 설치된 전체 구간
for i in range(k - 1):
    if i < n - 1:
        answer -= panel_list[i]         # 센서 사이 최대 구간 제외

print(answer)