import sys

""" 변수 정의 
m : 사대의 수 
n : 동물의 수 
l : 사정 거리 
m_list : 사대의 위치(오름 차순) 
x : 동물의 x좌표 
y : 동물의 y좌표
m_x : 사대의 x좌표
answer : 사냥한 동물의 수
"""

m, n, l = map(int, sys.stdin.readline().strip().split())
m_list = sorted(list(map(int, sys.stdin.readline().strip().split())))

# 동물의 x, y좌표 별로 이진 탐색 실시
answer = 0
for i in range(n):

    x, y = map(int, sys.stdin.readline().strip().split())

    min_m_x = -1

    # 동물의 x좌표와 가장 가까운 사대의 위치를 찾는 이진 탐색
    left = 0
    right = m - 1
    while left <= right:

        mid = (left + right) // 2

        if m_list[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1

        if min_m_x == - 1:
            min_m_x = abs(m_list[mid] - x)
        else:
            if abs(m_list[mid] - x) < min_m_x:
                min_m_x = abs(m_list[mid] - x)

    # print("x와 y 출력 :", x, y)
    # print("사대의 위치 :", min_m_x)
    # print("사대 까지의 거리 출력 :", abs((min_m_x - x)) + y)
    # print("---")

    if min_m_x + y <= l:
        answer += 1

print(answer)