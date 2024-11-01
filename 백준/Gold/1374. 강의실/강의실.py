import sys
import heapq

n = int(sys.stdin.readline().strip())
n_list = []
min_heap = []

for _ in range(n):

    lecture_number, start, end = map(int, sys.stdin.readline().strip().split())

    n_list.append((start, end))

n_list.sort()

max_lec = 0
for lecture in n_list:

    start, end = lecture

    while len(min_heap) != 0 and start >= min_heap[0]:    # 강의실을 더이상 안쓰는 강의들 제거
        heapq.heappop(min_heap)

    heapq.heappush(min_heap, end)

    max_lec = max(max_lec, len(min_heap))

print(max_lec)
