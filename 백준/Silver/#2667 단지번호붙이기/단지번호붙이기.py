import sys
import random

floor_max = int(sys.stdin.readline().strip())
room_max = floor_max
floor_dic = {}

for i in range(1, floor_max + 1):

    floor_input = sys.stdin.readline().strip()

    for j in range(1, room_max + 1):
        if floor_input[j - 1] == "1":
            floor_dic[str(i) + " " + str(j)] = []

for floor_room in floor_dic.keys():
    floor, room = map(int, floor_room.split())

    # 오른쪽 방과 관련한 키를 만듭니다.
    if room != room_max:
        right_room = str(floor) + " " + str(room + 1)
        # 옆방이 존재 한다면( 0 이 아니라면 ), 접근 가능한 방으로 현재 방의 값으로 추가 한다.
        if right_room in floor_dic.keys():
            floor_dic[floor_room].append(right_room)

    # 왼쪽 방과 관련한 키를 만듭니다.
    if room != 1:
        left_room = str(floor) + " " + str(room - 1)
        # 옆방이 존재 한다면, 접근 가능한 방으로 현재 방의 값으로 추가 한다.
        if left_room in floor_dic.keys():
            floor_dic[floor_room].append(left_room)

    # 위쪽 층의 방과 관련한 키를 만듭니다.
    if floor != 1:
        up_room = str(floor - 1) + " " + str(room)
        # 아래 층 방이 존재 한다면, 접근 가능한 방으로 현재 방의 값으로 추가 한다.
        if up_room in floor_dic.keys():
            floor_dic[floor_room].append(up_room)

    # 아래쪽 층의 방과 관련한 키를 만듭니다.
    if floor != floor_max:
        down_room = str(floor + 1) + " " + str(room)
        # 아래 층 방이 존재 한다면, 접근 가능한 방으로 현재 방의 값으로 추가 한다.
        if down_room in floor_dic.keys():
            floor_dic[floor_room].append(down_room)

bfs_queue = ["1 1"]
bfs_set = {"1 1"}
count_list = []

while len(floor_dic.keys()) != 0:

    count = 0
    # 무작위 키값을 가지고 온다. 또한 해당키로 bfs, 큐와 집합을 초기화 한다.
    random_floor_room = random.choice(list(floor_dic.keys()))
    bfs_queue = [random_floor_room]
    bfs_set = {random_floor_room}

    while len(bfs_queue) != 0:

        floor_room = bfs_queue.pop(0)

        for contact_room in floor_dic[floor_room]:
            # 현재 방에 연결된 방 중에 접근한적 없는 방이라면
            if contact_room not in bfs_set:
                # 이미 접근한 방으로서 기억함
                bfs_set.add(contact_room)
                # 접근한 방의 주변 방을 확인하기 위해서 저장
                bfs_queue.append(contact_room)

        count += 1
        floor_dic.pop(floor_room)

    count_list.append(count)

count_list.sort()

print(len(count_list))
for i in count_list:
    print(i)