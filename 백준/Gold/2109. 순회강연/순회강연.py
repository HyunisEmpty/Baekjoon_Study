import sys
import heapq

n = int(sys.stdin.readline().strip())
n_dict = dict()     # 각 날짜별 기한인 강연의 강연료를 저장
max_d = 0           # 기한이 가장긴 강연의 강연 기한

for _ in range(n):

    p, d = map(int, sys.stdin.readline().strip().split())

    max_d = max(max_d, d)   # 최대값 저장

    if d in n_dict: # 현재 날짜에 강의가 있다면
        n_dict[d].append(p)
    else:
        n_dict[d] = [p]

max_heap = []
answer = 0          # 최대 강연료를 저장
for i in range(max_d):

    day = max_d - i

    if day in n_dict:           # 현재 날짜가 강연 기한인 강연이 있는지
        for pay in n_dict[day]:     # 강연료
            heapq.heappush(max_heap, -pay)

    if len(max_heap) != 0:
        answer += -heapq.heappop(max_heap)

print(answer)