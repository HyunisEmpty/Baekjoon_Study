import sys
import heapq

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    n = int(sys.stdin.readline().strip())
    n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n//10 + 1)]

    max_heap = []   # 최대 힙
    min_heap = []   # 최소 힙
    median_list = []

    for number_list in n_list:
        for number in number_list:      # 모든 입력값에 한번씩 접근

            if len(max_heap) > len(min_heap):       # min_heap에 데이터 삽입
                heapq.heappush(min_heap, number)
            elif len(max_heap) == len(min_heap):    # max_haep에 데이터 삽입
                heapq.heappush(max_heap, -number)

                while len(max_heap) + len(min_heap) > 1 and -max_heap[0] > min_heap[0]:   # 최대 최소 힙 데이터 데이터 교체
                    max_heap_val = -heapq.heappop(max_heap)
                    min_heap_val = heapq.heappop(min_heap)
                    heapq.heappush(max_heap, -min_heap_val)
                    heapq.heappush(min_heap, max_heap_val)

                median_list.append(-max_heap[0])

    print(len(median_list))
    answer = ""
    for i in range(len(median_list)):
        if i % 10 == 0 and i != 0:
            print(answer)
            answer = str(median_list[i]) + " "
        else:
            answer += str(median_list[i]) + " "
    print(answer)