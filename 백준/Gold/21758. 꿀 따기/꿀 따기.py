import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().strip().split()))
sum_list = [0] + n_list

# 누적 합 연산
for i in range(1, n + 1):
    sum_list[i] += sum_list[i - 1]

# 벌1 벌2 통인 경우
left_max = 0
for i in range(2, len(sum_list) - 1):   # 벌통의 위치와 벌1의 위치는 제외

    bee1 = sum_list[len(sum_list) - 1] - sum_list[1] - n_list[i - 1]
    bee2 = sum_list[len(sum_list) - 1] - sum_list[i]

    left_max = max(bee1 + bee2, left_max)
    
# 벌1 통 벌2인 경우
mid_max = 0
for i in range(2, len(sum_list) - 1):   # 벌1과 벌2의 위치는 제외

    # 두 벌의 위치는 고정이고 통의 위치만 바꾸면 된다.
    bee1_bee2 = sum_list[len(sum_list) - 2] - sum_list[1] + n_list[i - 1]

    mid_max = max(bee1_bee2, mid_max)

# 통 벌1 벌2인 경우
right_max = 0
for i in range(2, len(sum_list) - 1):   # 벌통의 위치와 벌2의 위치는 제외

    bee1 = sum_list[i] - n_list[i - 1]
    bee2 = sum_list[len(sum_list) - 1] - n_list[len(sum_list) - 2] - n_list[i - 1]

    right_max = max(bee1 + bee2, right_max)

print(max(left_max, mid_max, right_max))