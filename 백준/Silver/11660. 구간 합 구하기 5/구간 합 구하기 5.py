import sys

n, m = map(int, sys.stdin.readline().split())
n_list = []

# 2차원 배열을 누적 합으로 저장
for i in range(n):
    n_list.append([0] + list(map(int, sys.stdin.readline().split())))

    for j in range(1, n + 1):
        n_list[i][j] += n_list[i][j - 1]

# 2차원 배열에 대한 누적 합 연산
for i in range(m):

    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    # 인덱스 좌표로 변환
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    answer = 0

    for x in range(x1, x2 + 1): # x2 좌표도 포함 해야 한다.
        answer += n_list[x][y2 + 1] - n_list[x][y1]

    print(answer)