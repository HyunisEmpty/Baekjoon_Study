import sys

n, m = map(int, sys.stdin.readline().split())
money_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

left = 1
right = sum(money_list)
min_money = 0

while left <= right:

    mid = (left + right) // 2
    now_money = mid
    index = 0
    m_count = 1  # now_money = mid에서 한번 인출 했으므로 1증가

    # N개의 사용할 금액을 순차적으로 받아와서 K(mid)에서 뺀다
    while index < n and m_count <= m:
        # 조건1 index는 N일 동안 사용할 돈이 있으므로 모두 순환해야 한다. 그전에 m_count가 m보다 커진다는건, 인출할 돈이 모자란 경우 밖에 없다.
        # 조건2 m_count가 m보다 커진 경우는, 인출할 돈이 모자란 경우밖에 없다.

        # 통장에서 뺀 돈으로 하루를 보낼 수 있는 경우
        if now_money >= money_list[index]:

            now_money -= money_list[index]

            # 다음날로 넘어간다.
            index += 1

        # 통장에서 뺀 돈으로 하루를 보낼 수 없는 경우:
        else:

            # 새로운 돈을 인출 한다.
            now_money = mid
            m_count += 1

    if m_count <= m:
        min_money = mid
        right = mid - 1
    else:
        left = mid + 1

print(min_money)
