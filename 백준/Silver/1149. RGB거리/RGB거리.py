import sys

""" 

변수 설명 
n : 집의 개수 
n_list : 중첩 리스트 각 집마다 색칠 하는 비용이 저장
dp_list : 현재 인덱스 부터 그 전 집까지의 비용의 합의 최솟값이 저장됨
min_cost : 비용의 최솟값이 저장됨

재귀 함수 인자 설명
before_index : 이전(인덱스) 집의 색깔
house_index : 현재집 인덱스(n_list에서) 
cost : 현재 까지 도색 하는데 들어간 비용
"""

n = int(sys.stdin.readline().strip())
n_list = []
dp_list = []
min_cost = -1

for i in range(n):
    n_list.append(list(map(int, sys.stdin.readline().strip().split())))
    dp_list.append([0, 0, 0])

# Dp 함수는 호출 되면 현재 인덱스의 값에 대해서 연산 시작,
def FindMinCost(before_color, house_index, cost):

    global min_cost
    global dp_list

    # 모든 집을 둘러본 경우 더이상 집을 그만 둘러 본다.
    if house_index == len(n_list):
        # 지금까지 최저 비용과 비교
        if min_cost == -1:
            min_cost = cost
        else:
            if cost < min_cost:
                min_cost = cost
        return

    for i in range(3):

        # 이전에 색칠할 색을 똑같이 색칠할 수는 없다.
        if i != before_color:

            if dp_list[house_index][i] != 0:

                # 현재 까지 집의 비용보다 싼 비용을 이전에 미리 찾은 경우
                if dp_list[house_index][i] <= n_list[house_index][i] + cost:
                    pass
                else:
                    dp_list[house_index][i] = n_list[house_index][i] + cost

                    # 재귀함수 호출
                    FindMinCost(i, house_index + 1, n_list[house_index][i] + cost)

            else:

                # 현재 까지 집의 비용까지 계산 한적없는 경우 새로 추가
                dp_list[house_index][i] = n_list[house_index][i] + cost

                # 재귀함수 호출
                FindMinCost(i, house_index + 1, n_list[house_index][i] + cost)

FindMinCost(-1, 0, 0)

print(min_cost)