import sys
import heapq

n = int(sys.stdin.readline().strip())   # 문제의 수
n_dict = dict()                         # 마감일 별 주어지는 라면의 수
max_day = 0                             # 마감일이 가장 긴 날을 저장
max_heap = []                           # 최대 힙, 현재 받을 수 있는 최대의 라면 저장
answer = 0

for _ in range(n):
    day, ramen = map(int, sys.stdin.readline().strip().split())

    max_day = max(max_day, day)

    if day not in n_dict:
        n_dict[day] = [ramen]
    else:
        n_dict[day].append(ramen)

for i in range(max_day):

    if max_day - i in n_dict:
        for ramen in n_dict[max_day - i]:

            heapq.heappush(max_heap, -ramen)

    if len(max_heap) != 0:
        answer += -heapq.heappop(max_heap)

print(answer)