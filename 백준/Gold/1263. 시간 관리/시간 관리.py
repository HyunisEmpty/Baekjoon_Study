import sys

n = int(sys.stdin.readline().strip())
n_list = []

for i in range(n):
    ti, si = map(int, sys.stdin.readline().split())
    n_list.append((ti, si))

# 마감 기한 si를 기준으로 내림차순으로 정렬 시킨다.
n_list.sort(key=lambda x: x[1], reverse=True)

# si를 기준으로 내림차순된 데이터를 반복문을 통해서 처리, 모든 문제를 최대한 늦게 처리하는 방식의 알고리즘
time = n_list[0][1]
for ti, si in n_list:

    # s(i-1) 이 si - ti보다 큰 경우 : 이는 다음 문제의 마감 시간(s(i-1))에 맞춰서 문제 해결을 시작 할 수 없으면 si - ti 시간에 맞춰서 문제해결을 시작해야 한다.
    if si > time:
        time = time - ti
    # s(i-1)가 si-ti보다 작거나 같은 경우 : 이는 다음 문제의 마감시간(s(i-1))에 맞춰서 문제 해결을 시작 할 수  있으면 s(i-1)시간에 맞춰서 문제 해결을 시작해야 한다.
    elif si <= time:
        time = si - ti

if time < 0:
    print(-1)
else:
    print(time)