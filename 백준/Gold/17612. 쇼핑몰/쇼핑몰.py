import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
min_heap = []   # 입장 관리
max_heap = []   # 퇴장 관리

for i in range(1, k + 1):
    # 튜플에는 무게, 계산대 번호, 고객번호 순으로 저장된다.
    heapq.heappush(min_heap, (0, i, 0))

for _ in range(n):
    customer_id, w = map(int, sys.stdin.readline().split())

    min_w, counter, min_id = min_heap[0]

    heapq.heapreplace(min_heap, (min_w + w, counter, customer_id))
    heapq.heappush(max_heap, (min_w + w, -1 * counter, customer_id))

answer = 0
for i in range(1, n + 1):
    w, counter, id = heapq.heappop(max_heap)

    answer += id * i

print(answer)
