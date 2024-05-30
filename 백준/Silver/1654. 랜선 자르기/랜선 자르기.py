import sys

k, n = map(int, sys.stdin.readline().split())
k_list = [int(sys.stdin.readline().strip()) for _ in range(k)]

start = 1
end = max(k_list)
max_cutter_cable = 0

# 랜선을 자를 최대 절단 길이를 구하는 이진 탐색
while start <= end:

    mid = (start + end)//2

    # 길이가 같은 cable의 개수
    cutter_cable = 0

    # mid로 k_cable을 자른 경우에 나오는 길이가 같은 랜선의 개수를 구하는 반복문
    for k_cable in k_list:
        cutter_cable += k_cable//mid

    # 자른 랜선의 개수가 목표값인 n보다 작은 경우(많이 자른 경우, 탐색 범위 감소)
    if cutter_cable < n:
        end = mid - 1
    # 자른 랜선의 개수가 목표값인 n보다 큰 경우(조금 자른 경우, 탐색 범위 증가)
    else:
        start = mid + 1

        # 현재 절단한 케이블 길이가, 최대 절단 케이블 길이보다 길다면 최대값을 업데이트
        if max_cutter_cable < mid:
            max_cutter_cable = mid

print(max_cutter_cable)