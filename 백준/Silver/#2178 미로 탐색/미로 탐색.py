import sys

floor_max, room_max = map(int, sys.stdin.readline().split())
floor_dic = {}
floor_count_dic = {}

for i in range(1, floor_max + 1):

    floor_input = sys.stdin.readline().strip()

    for j in range(1, room_max + 1):
        if floor_input[j - 1] == "1":
            floor_dic[str(i) + " " + str(j)] = []
            floor_count_dic[str(i) + " " + str(j)] = 0


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
floor_count_dic["1 1"] = 1

while True:
    floor_room = bfs_queue.pop(0)

    if floor_room == str(floor_max) + " " + str(room_max):
        break

    for contact_room in floor_dic[floor_room]:
        # 현재 방에 연결된 방 중에 접근한 적 없는 방이라면
        if contact_room not in bfs_set:
            floor_count_dic[contact_room] = floor_count_dic[floor_room] + 1
            bfs_set.add(contact_room)
            bfs_queue.append(contact_room)

print(floor_count_dic[str(floor_max) + " " + str(room_max)])