import sys
import heapq

n = int(sys.stdin.readline().strip())   # 전체 회의실의 개수
min_heap = []

for _ in range(n):

    # 강의 종료, 시작시간으로 분활
    start, end = map(int, sys.stdin.readline().split())

    heapq.heappush(min_heap, (end, start))

now_time = 0
cnt = 0
while min_heap:

    # 현재 가장 빨리 끝나는 강의 시간
    end, start = heapq.heappop(min_heap)

    # 강의를 시작 가능할때
    if start >= now_time:
        now_time = end
        cnt += 1

print(cnt)