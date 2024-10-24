import heapq
import sys

maxqueue = []
n = int(sys.stdin.readline().strip())

for i in range(n):
    data = int(sys.stdin.readline().strip())

    if data == 0:
        if len(maxqueue) == 0:
            print(0)
        else:
            print(heapq.heappop(maxqueue))
    else:
        heapq.heappush(maxqueue, data)