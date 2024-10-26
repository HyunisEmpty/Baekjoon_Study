import sys
import heapq
import copy

n = int(sys.stdin.readline().strip())

max_heap = []
min_heap = []

for i in range(n):

    k = int(sys.stdin.readline().strip())

    # 최대, 최소 힙에 데이터 추가
    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, k)
    elif len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -k)

    # 데이터 교환
    while len(max_heap) + len(min_heap) > 1 and -max_heap[0] > min_heap[0]:
        max_val = copy.deepcopy(-max_heap[0])
        min_val = copy.deepcopy(min_heap[0])

        heapq.heapreplace(min_heap, max_val)
        heapq.heapreplace(max_heap, -min_val)

    print(-max_heap[0])