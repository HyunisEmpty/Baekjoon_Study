import sys
import heapq


n = int(sys.stdin.readline().strip())
min_heap = []

for _ in range(n):

    n_list = list(map(int, sys.stdin.readline().strip().split()))

    for target in n_list:
        if len(min_heap) != n:
            heapq.heappush(min_heap, target)
        else:
            if target > min_heap[0]:    # 삽입 연산
                heapq.heappushpop(min_heap, target)

print(min_heap[0])

