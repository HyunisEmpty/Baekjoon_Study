import sys

n = int(sys.stdin.readline().strip())
n_list = [0]
for i in range(n):
    n_list.append(int(sys.stdin.readline().strip()))
n_memo_list = [[0, 0] for _ in range(n + 1)]

# 인자 값으로는 현재 몇번째 계단에 인지와 현재 계단을 올라오며 모은 점수 그리고 연속해서 계단 하나를 올라온 횟수가 저장되어 있다.
def StepStairs(now_stair, score, cnt, bug_list):

    global n_list
    global n_memo_list

    # 메모 제이션
    # 이전 값보다 작은 경우 연산을 종료 시킨다.
    if score < n_memo_list[now_stair][cnt - 1]:
        return
    # 이전 값보다 큰 경우 최댓값 업데이트
    else:
        n_memo_list[now_stair][cnt - 1] = score

    # 종료 조건
    if now_stair == n:
        return

    # 재귀 호출
    if cnt < 2:
        if now_stair + 1 <= n:

            StepStairs(now_stair + 1, score + n_list[now_stair + 1], cnt + 1, bug_list + [n_list[now_stair + 1]])
    if now_stair + 2 <= n:
        StepStairs(now_stair + 2, score + n_list[now_stair + 2], 1, bug_list + [n_list[now_stair + 2]])


StepStairs(0, 0, 0, [])
print(max(n_memo_list[n][0], n_memo_list[n][1]))