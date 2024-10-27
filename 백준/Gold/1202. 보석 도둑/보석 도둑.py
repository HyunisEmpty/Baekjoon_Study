import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
n_list = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)])
k_list = sorted([int(sys.stdin.readline().strip()) for _ in range(k)])

max_heap = []   # 무게 제한을 만족하는 보석의 가치를 저장하는 최대 힙
n_index = 0
answer = 0

for weight_limit in k_list:

    while n_index < n and weight_limit >= n_list[n_index][0]:       # 현재 무게 제한 보다 무게가 작은 보석 이라면
        heapq.heappush(max_heap, -n_list[n_index][1])
        n_index += 1

    if len(max_heap) != 0:
        answer += -heapq.heappop(max_heap)

print(answer)