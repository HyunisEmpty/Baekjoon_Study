import sys
import random

while True:
    land_dic = {}

    w, h = map(int, sys.stdin.readline().split())

    if w + h == 0:
        break

    for i in range(h):
        sea_list = list(map(int, sys.stdin.readline().split()))
        for j in range(w):
            if sea_list[j] == 1:
                land_dic[str(i) + " " + str(j)] = []

    for land in land_dic.keys():
        height, weight = map(int, land.split())

        # 오른쪽 섬과 관련한 키를 만듭니다.
        right_land = str(height) + " " + str(weight + 1)
        if right_land in land_dic.keys():
            land_dic[land].append(right_land)

        # 왼쪽 섬과 관련한 키를 만듭니다.
        left_land = str(height) + " " + str(weight - 1)
        if left_land in land_dic.keys():
            land_dic[land].append(left_land)

        # 위쪽 섬과 관련한 키를 만듭니다.
        up_land = str(height - 1) + " " + str(weight)
        if up_land in land_dic.keys():
            land_dic[land].append(up_land)

        # 아래쪽 섬과 관련한 키를 만듭니다.
        down_land = str(height + 1) + " " + str(weight)
        if down_land in land_dic.keys():
            land_dic[land].append(down_land)

        # 오른쪽 위 섬과 관련한 키를 만듭니다.
        right_land = str(height + 1) + " " + str(weight + 1)
        if right_land in land_dic.keys():
            land_dic[land].append(right_land)

        # 왼쪽 위 섬과 관련한 키를 만듭니다.
        left_land = str(height + 1) + " " + str(weight - 1)
        if left_land in land_dic.keys():
            land_dic[land].append(left_land)

        # 오른쪽 아래 섬과 관련한 키를 만듭니다.
        right_land = str(height - 1) + " " + str(weight + 1)
        if right_land in land_dic.keys():
            land_dic[land].append(right_land)

        # 왼쪽 아래 섬과 관련한 키를 만듭니다.
        left_land = str(height - 1) + " " + str(weight - 1)
        if left_land in land_dic.keys():
            land_dic[land].append(left_land)


    # BFS 알고리즘
    count = 0
    while len(land_dic.keys()) != 0:
        random_land = random.choice(list(land_dic.keys()))
        bfs_queue = [random_land]
        bfs_set = {random_land}

        while len(bfs_queue) != 0:
            land = bfs_queue.pop(0)
            for contact_land in land_dic[land]:
                if contact_land not in bfs_set:
                    bfs_set.add(contact_land)
                    bfs_queue.append(contact_land)
            land_dic.pop(land)
        count += 1

    print(count)
