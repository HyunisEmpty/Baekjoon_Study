# 선택 정렬
import sys

n = int(sys.stdin.readline().strip())

number_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

for i in range(n-1):
    # 최솟갑을 정렬되지 않은 부분의 첫번째 값으로 변경
    min_num = number_list[i]

    for j in range(i, n):
        if number_list[j] < min_num:
            min_num, number_list[j] = number_list[j], min_num

    number_list[i] = min_num

for count in range(n):
    print(number_list[count])
