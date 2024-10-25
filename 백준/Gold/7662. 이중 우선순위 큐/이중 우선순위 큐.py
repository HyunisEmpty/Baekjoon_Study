import sys
import heapq

test_case = int(sys.stdin.readline().strip())
for test in range(test_case):

    max_heap = []       # 최대 힙
    max_dic = dict()    # 최대 힙 제거 연산 정보 저장
    min_heap = []       # 최소 힙
    min_dic = dict()    # 최소 힙 제거 연산 정보 저장

    command_cnt = int(sys.stdin.readline().strip())     # 명령 횟수
    for _ in range(command_cnt):                        # 명령 횟수 만큼 실행

        command, number = map(str, sys.stdin.readline().split())    # 명령 분활
        number = int(number)

        if command == "I":  # 삽입 연산
            heapq.heappush(max_heap, -number)   # 최대 힙 삽입 연산
            heapq.heappush(min_heap, number)    # 최소 힙 삽입 연산

        elif command == "D": # 제거 연산
            if number == 1:     # 최댓값 제거

                # 최소 힙과 동기화 연산
                while len(max_heap) > 0 and -max_heap[0] in min_dic:
                    min_dic[-max_heap[0]] -= 1   # 동기화 진행
                    if min_dic[-max_heap[0]] == 0:
                        del min_dic[-max_heap[0]]
                    heapq.heappop(max_heap)

                # 최대 힙 루트 노드 제거
                if len(max_heap) > 0:
                    max_val = -heapq.heappop(max_heap)
                    if max_val in max_dic:
                        max_dic[max_val] += 1
                    else:
                        max_dic[max_val] = 1

            elif number == -1:  # 최솟값 제거

                # 최대 힙과 동기화 연산
                while len(min_heap) > 0 and min_heap[0] in max_dic:
                    max_dic[min_heap[0]] -= 1   # 동기화 진행
                    if max_dic[min_heap[0]] == 0:
                        del max_dic[min_heap[0]]
                    heapq.heappop(min_heap)

                # 최소 힙 루트 노드 제거
                if len(min_heap) > 0:
                    min_val = heapq.heappop(min_heap)
                    if min_val in min_dic:
                        min_dic[min_val] += 1
                    else:
                        min_dic[min_val] = 1

    # 최소 힙과 동기화 연산
    while len(max_heap) > 0 and -max_heap[0] in min_dic:
        min_dic[-max_heap[0]] -= 1  # 동기화 진행
        if min_dic[-max_heap[0]] == 0:
            del min_dic[-max_heap[0]]
        heapq.heappop(max_heap)

    # 최대 힙과 동기화 연산
    while len(min_heap) > 0 and min_heap[0] in max_dic:
        max_dic[min_heap[0]] -= 1  # 동기화 진행
        if max_dic[min_heap[0]] == 0:
            del max_dic[min_heap[0]]
        heapq.heappop(min_heap)

    if len(max_heap) + len(min_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])

