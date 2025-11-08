import sys

test_case = int(sys.stdin.readline().strip())

for _ in range(test_case):
    n = int(sys.stdin.readline().strip())
    cost_single, cost_half = map(int, sys.stdin.readline().split())

    total_cost = 0

    # n을 0이 될 때까지 1씩 줄이거나 /2 하는 과정
    while n > 0:

        # 홀수면 1을 빼는 것이 강제됨
        if n % 2 == 1:
            n -= 1
            total_cost += cost_single

        # 짝수면 절반으로 줄이기와 1씩 깎기 중 저렴한 것을 선택
        else:
            half_n = n // 2
            total_cost += min(half_n * cost_single, cost_half)
            n = half_n

    print(total_cost)