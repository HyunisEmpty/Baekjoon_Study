import sys
import heapq

n = int(sys.stdin.readline().strip())   # 회의 개수 저장
n_list = []                             # 회의 시작, 종료시간 저장
min_heapq = []                          # 진행중인 회의들 저장

for _ in range(n):      # 회의 입력
    start, end = map(int, sys.stdin.readline().strip().split())
    n_list.append([start, end])

n_list.sort()

max_cnt = 0
for meeting_room in n_list:
    start, end = meeting_room

    if len(min_heapq) == 0:             # 어떤 회의실도 사용하지 않는 경우
        heapq.heappush(min_heapq, end)
    else:
        while len(min_heapq) != 0 and min_heapq[0] <= start:    # 현재회의실을 사용 가능한 경우
            heapq.heappop(min_heapq)
        heapq.heappush(min_heapq, end)  # 현재 회의 진행

    max_cnt = max(max_cnt, len(min_heapq))  # 최대 사용한 회의실 수 저장

print(max_cnt)