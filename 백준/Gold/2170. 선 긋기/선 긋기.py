import sys

N = int(sys.stdin.readline().strip())
point_list = [] # 좌표 저장할 리스트
total_length = 0

# 입력 처리 for문
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    point_list.append((start, end))

# x 좌표 기준 정렬
point_list.sort()

# 시작 좌표 설정
start_position, end_position = 0, 0
for now_start, now_end in point_list:

    # if start_position == 0 and end_position == 0:
    #     start_position = now_start
    #     end_position = now_end

    if start_position <= now_start <= end_position:
        if end_position <= now_end:
            end_position = now_end
    else:
        total_length += end_position - start_position
        start_position = now_start
        end_position = now_end

# if start_position == 0 and end_position == 0:
#     start_position = now_start
#     end_position = now_end

total_length += end_position - start_position
print(total_length)