import sys

""" 변수 정의 
m : 사대의 수 
n : 동물의 수 
l : 사정 거리 
m_list : 사대의 위치(오름차순) 
x : 동물의 x좌표 
y : 동물의 y좌표
m_x : 사대의 위치
hunt_count : 사냥한 동물의 수
"""

m, n, l = map(int, sys.stdin.readline().strip().split())
m_list = sorted(list(map(int, sys.stdin.readline().strip().split())))

# 동물 위치 입력
hunt_count = 0
for i in range(n):

    x, y = map(int, sys.stdin.readline().strip().split())

    left = 0
    right = m - 1

    if m == 1:
        m_x = m_list[0]
    else:
        m_x = 0

    while left <= right:

        mid = (left + right) // 2

        if m_list[mid] >= x:
            m_x = m_list[mid]
            right = mid - 1
        else:
            left = mid + 1

    # print("x와 y 출력 :", x, y)
    # print("사대의 위치 :", m_x)
    # print("사대 까지의 거리 출력 :", abs(m_x - x), abs((m_x - x)) + y)
    # print()

    if abs(m_x - x) + y <= l:
        hunt_count += 1

print(hunt_count)