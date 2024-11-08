import sys
import heapq

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().split()))

min_heap = []       # 최소 힙
for i in range(n):  # 수열 최소 힙에 저장
    heapq.heappush(min_heap, (n_list[i], i))

query = int(sys.stdin.readline().strip())
for _ in range(query):      # 쿼리의 수 만큼 수행

    query_list = list(map(int, sys.stdin.readline().split()))

    if query_list[0] == 1:      # 값 변경 연산
        index = query_list[1] - 1
        value = query_list[2]

        n_list[index] = value
        heapq.heappush(min_heap, (value, index))
    elif query_list[0] == 2:        # 최소 값 인덱스 출력 연산

        while min_heap[0][0] != n_list[min_heap[0][1]]:
            heapq.heappop(min_heap)

        print(min_heap[0][1] + 1)
