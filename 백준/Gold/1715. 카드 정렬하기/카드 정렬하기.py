import sys
import heapq

n = int(sys.stdin.readline().strip())
heap_queue = []
for i in range(n):
    heapq.heappush(heap_queue, int(sys.stdin.readline().strip()))

answer = 0
while len(heap_queue) >= 2:

    number1 = heapq.heappop(heap_queue)
    number2 = heapq.heappop(heap_queue)
    answer += number1 + number2
    heapq.heappush(heap_queue, number1 + number2)

print(answer)



