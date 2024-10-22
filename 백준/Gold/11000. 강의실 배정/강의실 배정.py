import sys
import heapq

n = int(sys.stdin.readline().strip())
n_list = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    n_list.append((a, b))
n_list.sort()

class_room_list = []
for lecture in n_list:
    start, end = lecture

    if len(class_room_list) == 0:
        heapq.heappush(class_room_list, end)
    else:
        if class_room_list[0] > start:  # 만약 현재 강의를 수업할 수 있는 강의실이 없는 경우
            heapq.heappush(class_room_list, end)
        else:                           # 현재 강의를 수업할 수 있다면
            heapq.heappushpop(class_room_list, end)

print(len(class_room_list))
