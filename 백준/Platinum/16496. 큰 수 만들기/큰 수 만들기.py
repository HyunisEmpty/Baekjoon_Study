import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(str, sys.stdin.readline().strip().split()))
n_visited = [False for _ in range(n)]
answer_list = []

while True:
    a = -1
    b = -1

    for i in range(n):      # a와 b에 사용한적 없는 수의 인덱스를 저장
        if n_list[i] != "" and a == -1:     # 이미 사용한 수가 아니라면
            a = i                           # 사용가능한 값의 인덱스 저장
        elif n_list[i] != "" and b == -1 and a != -1:     # 사용한 수가 아니며 a가 접근한 수가 아니라면
            b = i                           # b다음 사용가능한 값의 인덱스 저장
            break

    if b == -1: # 만약 더이상 사용할 수 있는 수가 없다면 a는 있을 수도  있음
        answer_list.append(n_list[a])
        break

    while b != n:   # b만 움직이며 그 값을 비교하여 a에 최대의 인덱스 값이 저장됨

        if n_list[b] != "":     # 현재 b값이
            if int(n_list[a] + n_list[b]) < int(n_list[b] + n_list[a]):
                a = b
            elif int(n_list[a] + n_list[b]) > int(n_list[b] + n_list[a]):
                pass
        b += 1

    answer_list.append(n_list[a])
    n_list[a] = ""

answer = ""
for number in answer_list:
    answer += number

if int(answer) == 0:
    print(0)
else:
    print(answer)
