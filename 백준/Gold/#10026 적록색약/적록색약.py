import sys
import random

n = int(sys.stdin.readline().strip())

color_list = []
color_blind_list = []
color_tree_dic = {}
color_blind_tree_dic = {}

# 색맹일 때와 아닐 때의 리스트를 만든다
for i in range(n):
    blind_input = ""
    input = sys.stdin.readline().strip()
    for j in range(n):
        if input[j] == "R":
            blind_input += "G"
        else:
            blind_input += input[j]
    color_list.append(input)
    color_blind_list.append(blind_input)

# 색맹이 아닐 때와 색맹일 때 키를 저장
for i in range(n):
    for j in range(n):
        color = color_list[i][j]
        color_tree_dic[color + " " + str(i) + " " + str(j)] = []
        color_blind = color_blind_list[i][j]
        color_blind_tree_dic[color_blind + " " + str(i) + " " + str(j)] = []

# 인접한 색과 관련한 키를 저장합니다.
for i in range(n):
    for j in range(n):
        color = color_list[i][j]
        color_blind = color_blind_list[i][j]

        now_color = color + " " + str(i) + " " + str(j)
        now_color_blind = color_blind + " " + str(i) + " " + str(j)

        # 오른쪽 색깔과 관련한 키를 만듭니다.
        right_color = color + " " + str(i) + " " + str(j + 1)
        right_color_blind = color_blind + " " + str(i) + " " + str(j + 1)
        if right_color in color_tree_dic.keys():
            color_tree_dic[now_color].append(right_color)
        if right_color_blind in color_blind_tree_dic.keys():
            color_blind_tree_dic[now_color_blind].append(right_color_blind)

        # 왼쪽 색깔과 관련한 키를 만듭니다.
        left_color = color + " " + str(i) + " " + str(j - 1)
        left_color_blind = color_blind + " " + str(i) + " " + str(j - 1)
        if left_color in color_tree_dic.keys():
            color_tree_dic[now_color].append(left_color)
        if left_color_blind in color_blind_tree_dic.keys():
            color_blind_tree_dic[now_color_blind].append(left_color_blind)

        # 위쪽 색깔과 관련한 키를 만듭니다.
        up_color = color + " " + str(i + 1) + " " + str(j)
        up_color_blind = color_blind + " " + str(i + 1) + " " + str(j)
        if up_color in color_tree_dic.keys():
            color_tree_dic[now_color].append(up_color)
        if up_color_blind in color_blind_tree_dic.keys():
            color_blind_tree_dic[now_color_blind].append(up_color_blind)

        # 아래쪽 색깔과 관련한 키를 만듭니다.
        down_color = color + " " + str(i - 1) + " " + str(j)
        down_color_blind = color_blind + " " + str(i - 1) + " " + str(j)
        if down_color in color_tree_dic.keys():
            color_tree_dic[now_color].append(down_color)
        if down_color_blind in color_blind_tree_dic.keys():
            color_blind_tree_dic[now_color_blind].append(down_color_blind)

# BFS 알고리즘 ( 색맹이 아닌 경우 )
color_count = 0
while len(color_tree_dic.keys()) != 0:
    # 무작위 키값을 가지고 온다. 또한 해당키로 bfs, 큐와 집합을 초기화 한다.
    random_color = random.choice(list(color_tree_dic.keys()))
    bfs_color_queue = [random_color]
    bfs_color_set = {random_color}

    while len(bfs_color_queue) != 0:

        color = bfs_color_queue.pop(0)

        for contact_color in color_tree_dic[color]:
            # 현재 방에 연결된 방 중에 접근한적 없는 방이라면
            if contact_color not in bfs_color_set:
                # 이미 접근한 방으로서 기억함
                bfs_color_set.add(contact_color)
                # 접근한 방의 주변 방을 확인하기 위해서 저장
                bfs_color_queue.append(contact_color)

        color_tree_dic.pop(color)

    color_count += 1

# BFS 알고리즘 ( 색맹인 경우 )
color_blind_count = 0
while len(color_blind_tree_dic.keys()) != 0:
    # 무작위 키값을 가지고 온다. 또한 해당키로 bfs, 큐와 집합을 초기화 한다.
    random_color_blind = random.choice(list(color_blind_tree_dic.keys()))
    bfs_color_blind_queue = [random_color_blind]
    bfs_color_blind_set = {random_color_blind}

    while len(bfs_color_blind_queue) != 0:

        color_blind = bfs_color_blind_queue.pop(0)

        for contact_color_blind in color_blind_tree_dic[color_blind]:
            # 현재 색에 인접한 색중 접근한적 없는 색이라면
            if contact_color_blind not in bfs_color_blind_set:
                # 이미 접근한 색으로 기억함
                bfs_color_blind_set.add(contact_color_blind)
                # 접근한 색의 주변 색을 확인하기 위해서 저장
                bfs_color_blind_queue.append(contact_color_blind)

        color_blind_tree_dic.pop(color_blind)

    color_blind_count += 1

print(color_count, color_blind_count)