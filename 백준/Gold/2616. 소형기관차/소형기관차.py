import sys

N = int(sys.stdin.readline().strip())
people_list = list(map(int, sys.stdin.readline().split()))
people_list.insert(0, 0)              # 1-based 인덱스 맞추기
segment_len = int(sys.stdin.readline().strip())  # 한 기관차가 차지하는 구간 길이

# prefix_sum_list[i] = 1..i까지의 누적 승객 수
prefix_sum_list = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum_list[i] = prefix_sum_list[i - 1] + people_list[i]

# dp_table[k][j] = k개의 구간(기관차)을 고려했을 때, 1..j까지에서 얻을 수 있는 최대 승객 수
dp_table = [[0] * (N + 1) for _ in range(4)]

# DP 전개: 각 기관차 개수별로 오른쪽으로 진행하며 최적값 갱신
for k in range(1, 4):
    # j는 구간의 끝 인덱스(구간 길이(segment_len)부터 시작해야 구간을 완성할 수 있음)
    for j in range(segment_len, N + 1):
        # 현재 위치에 구간을 배치했을 때 얻는 값:
        # 이전 k-1개의 구간에서 j-segment_len까지 최적값 + (j-segment_len+1 .. j)의 승객 합
        current_segment_sum = prefix_sum_list[j] - prefix_sum_list[j - segment_len]
        take_segment = dp_table[k - 1][j - segment_len] + current_segment_sum

        # j 위치까지 고려했을 때의 최댓값은
        dp_table[k][j] = max(dp_table[k][j - 1], take_segment)

# 최종: 3개의 구간을 사용해 1..N에서 얻을 수 있는 최대 승객 수
print(dp_table[3][N])

