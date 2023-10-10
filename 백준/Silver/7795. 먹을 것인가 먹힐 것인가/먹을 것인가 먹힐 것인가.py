import sys

test_case = int(sys.stdin.readline())

for test in range(test_case):
    N, M = map(int, sys.stdin.readline().split())
    a_list = list(map(int, sys.stdin.readline().split()))
    b_list = list(map(int, sys.stdin.readline().split()))
    b_index = 0 # 현재 a와 비교하는 b의 인덱스 번호를 저장합니다.
    count = 0 # 현재 a보다 큰 B의 개수를 저장합니다.
    answer = 0 # 출력하고자하는 정답을 저장합니다.

    a_list.sort(reverse=True)
    b_list.sort(reverse=True)

    for a in a_list:

        while M > b_index and b_list[b_index] >= a:
            count += 1
            b_index += 1
        else:
            answer += M - count

    print(answer)
