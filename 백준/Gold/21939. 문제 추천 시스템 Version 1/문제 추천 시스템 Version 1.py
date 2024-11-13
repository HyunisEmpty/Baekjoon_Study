import sys
import heapq

min_heap = []
max_heap = []
recommend_set = set()
recommend_dic = dict()

n = int(sys.stdin.readline().strip())
for _ in range(n):

    P, L = map(int, sys.stdin.readline().strip().split())

    heapq.heappush(min_heap, (L, P))
    heapq.heappush(max_heap, (-L, -P))
    recommend_set.add((L, P))
    recommend_dic[P] = L

command_cnt = int(sys.stdin.readline().strip())
for _ in range(command_cnt):

    command = list(map(str, sys.stdin.readline().strip().split()))

    # print(" ".join(command))
    # print("set",recommend_set)
    # print("dict", recommend_dic)

    if command[0] == "recommend":   # 문제 출력

        if int(command[1]) == 1:        # 가장 어려운 문제의 번호를 출력

            while True:     # 이미 제거된 값이 루트노드에 있는 경우 제거
                L, P = max_heap[0]
                if (-L, -P) not in recommend_set:     # 이미 제거된 문제인 경우
                    heapq.heappop(max_heap)     # 값 제거
                else:
                    break

            print(-max_heap[0][1])

        elif int(command[1]) == -1:     # 가장 쉬운 문제의 번호를 출력

            while True:     # 이미 제거된 값이 루트노드에 있는 경우 제거
                L, P = min_heap[0]
                if (L, P) not in recommend_set:     # 이미 제거된 문제인 경우
                    heapq.heappop(min_heap)     # 값 제거
                else:
                    break

            print(min_heap[0][1])

    elif command[0] == "solved":        # 추천 문제 리스트에서 문제 번호 P를 추가

        P = int(command[1])         # 문제 번호
        L = int(recommend_dic[P])

        if (L, P) in recommend_set:
            recommend_set.remove((L, P))
        if P in recommend_dic:
            recommend_dic.pop(P)

    elif command[0] == "add":           # 추천 문제 리스트에 P L 추가

        P = int(command[1])
        L = int(command[2])

        heapq.heappush(min_heap, (L, P))
        heapq.heappush(max_heap, (-L, -P))
        recommend_set.add((L, P))
        recommend_dic[P] = L