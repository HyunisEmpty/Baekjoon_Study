import sys

n, h = map(int, sys.stdin.readline().split())
up_list = [0] * h   # 석순 리스트
down_list = [0] * h # 종유석 리스트
sum_list = [0] * h # 석순 + 종유석 리스트
down_cnt = up_cnt = n//2
answer = 0
answer_cnt = 0

for i in range(1, n + 1):

    # 홀수, 석순인 경우
    if i % 2 == 1:
        up_list[int(sys.stdin.readline().strip()) - 1] += 1

    # 짝수, 종유석인 경우
    else:
        down_list[(h - 1) - (int(sys.stdin.readline().strip()) - 1)] += 1

for i in range(h):

    # 높이별 석순이 중첩된 개수를 저장
    up_cnt = up_cnt - up_list[i]
    up_list[i] += up_cnt

    # 높이별 종유석이 중첩된 개수를 저장
    down_cnt = down_cnt - down_list[(len(down_list) - 1) - i]
    down_list[(len(down_list) - 1) - i] += down_cnt

    sum_list[i] += up_list[i]
    sum_list[(len(down_list) - 1) - i] += down_list[(len(down_list) - 1) - i]

for i in range(h):

    if i == 0:
        answer = sum_list[i]
        answer_cnt = 1
    else:
        if sum_list[i] < answer:
            answer = sum_list[i]
            answer_cnt = 1
        elif sum_list[i] == answer:
            answer_cnt += 1

print(answer, answer_cnt)