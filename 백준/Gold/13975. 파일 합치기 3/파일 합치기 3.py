import sys
import heapq

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    n = int(sys.stdin.readline().strip())

    min_heapq = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(min_heapq)

    answer = 0

    while len(min_heapq) > 1:   # 하나의 수 가 남으면 연산을 종료

        number1 = heapq.heappop(min_heapq)
        number2 = heapq.heappop(min_heapq)

        heapq.heappush(min_heapq, number1 + number2)

        answer += number1 + number2

    print(answer)