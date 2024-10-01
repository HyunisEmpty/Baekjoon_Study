import sys

n, m = map(int, sys.stdin.readline().split())
m_list = [int(sys.stdin.readline().strip()) for i in range(m)]
m_list.sort()

# pi의 최솟값부터 pi의 최댓값 까지 접근
max_income = 0  # 수익이 최대가 되는 경우를 저장
max_i = 0       # 최대로 책정된 달걀 가격
for i in range(m_list[0], m_list[-1]+1):

    # 모든 pi에 접근
    income = 0
    cnt = 0
    for pi in m_list:

        # 달걀을 팔 수 있다면
        if pi >= i:
            income += i
            cnt += 1

        # 가지고 있는 달걀을 전부 팔았다면
        if cnt == n:
            break

    if income > max_income:
        max_income = income
        max_i = i

print(max_i, max_income)