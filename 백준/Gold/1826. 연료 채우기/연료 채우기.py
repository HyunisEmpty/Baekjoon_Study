import sys
import heapq

n = int(sys.stdin.readline().strip())

min_heap = []   # 가까운 주유소 부터 접근하기 위한 min_heap
for _ in range(n):
    distance, oil = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(min_heap, (distance, oil))

l, p = map(int, sys.stdin.readline().strip().split())   # 마을 까지의 거리, 기존 트럭 연료 입력

max_heap = []
cnt = 0
while p < l:

    while len(min_heap) != 0 and min_heap[0][0] <= p:

        distance, oil = heapq.heappop(min_heap)     # 이동 거리 내에 있는 주요소와 기름 정보

        heapq.heappush(max_heap, -oil)

    if len(max_heap) != 0:  # 주유소를 방문해야 하는 경우
        p += -heapq.heappop(max_heap)
        cnt += 1
    else:                   # 주유소가 없는 경우
        break

if p < l:
    print(-1)
else:
    print(cnt)