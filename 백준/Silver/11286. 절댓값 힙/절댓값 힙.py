import sys
import heapq

n = int(sys.stdin.readline().strip())
min_heap = []
for _ in range(n):

    number = int(sys.stdin.readline().strip())

    if number != 0:     # 값이 입력 일때
        heapq.heappush(min_heap, (abs(number), number))
    else:               # 값을 출력 할때

        if len(min_heap) == 0:
            print(0)
        else:
            abs_root, root = heapq.heappop(min_heap)
            print(root)