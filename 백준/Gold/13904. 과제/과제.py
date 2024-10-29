import sys
import heapq

n = int(sys.stdin.readline().strip())
max_heap = []

max_day = 0         # 가장 마감 일이 긴 과제
n_dic = dict()      # 마감일 별 과제 점수를 저장
for _ in range(n):      # 입력 처리
    day, score = map(int, sys.stdin.readline().strip().split())

    if max_day < day:
        max_day = day

    if day not in n_dic:        # 과제 마감 일을 키로, 점수를 값으로 리스트에 저장
        n_dic[day] = [score]
    else:
        n_dic[day].append(score)

best_score = 0          # 총 점수 저장
for today in range(max_day):    # 마감일 부터 현재 까지 하루씩 접근

    today = max_day - today

    if today in n_dic:
        for today_score in n_dic[today]:
            heapq.heappush(max_heap, -today_score)

    if len(max_heap) != 0:
        best_score += -heapq.heappop(max_heap)

print(best_score)


