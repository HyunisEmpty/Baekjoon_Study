import sys

# 입력 처리
n = int(sys.stdin.readline().strip())

MOD = 10 ** 9
num_count = 10                       # 숫자 범위 0~9
bit_count = 1 << num_count           # 비트마스크 총 상태 수 (0b0000000000 ~ 0b1111111111)
# DP 테이블 정의: dp_table[length][last_digit][bitmask]
# length 길이의 수 중 마지막 숫자가 last_digit이며, 사용된 숫자 상태가 bitmask인 경우의 수
dp_table = [[[0] * bit_count for _ in range(num_count)] for _ in range(n + 1)]

# 한 자리 수 초기화 (1~9까지, 0으로 시작하는 수는 제외)
for digit in range(1, num_count):
    dp_table[1][digit][1 << digit] = 1

# DP 진행
for length in range(1, n):
    for last_digit in range(num_count):
        for bitmask in range(bit_count):
            current_count = dp_table[length][last_digit][bitmask]
            if current_count == 0:
                continue

            # 인접한 자리수로 이동: last_digit + 1 또는 last_digit - 1
            # 다음 자리수를 포함한 비트마스크로 업데이트
            if last_digit + 1 < num_count:
                next_bitmask = bitmask | (1 << (last_digit + 1))
                dp_table[length + 1][last_digit + 1][next_bitmask] += current_count
                dp_table[length + 1][last_digit + 1][next_bitmask] %= MOD

            if last_digit - 1 >= 0:
                next_bitmask = bitmask | (1 << (last_digit - 1))
                dp_table[length + 1][last_digit - 1][next_bitmask] += current_count
                dp_table[length + 1][last_digit - 1][next_bitmask] %= MOD

# 모든 자리(0~9)가 한 번 이상 등장한 경우의 수 계산
all_used_mask = (1 << num_count) - 1
total_count = 0
for last_digit in range(num_count):
    total_count = (total_count + dp_table[n][last_digit][all_used_mask]) % MOD

print(total_count)
# 디버깅용 출력
# print(dp_table)

