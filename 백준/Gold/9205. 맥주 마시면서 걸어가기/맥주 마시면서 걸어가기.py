import sys

test = int(sys.stdin.readline().strip())

for test_case in range(test):

    # 집,편의점, 펜타포트의 수
    n = int(sys.stdin.readline().strip())
    store_list = []     # 편의점 x, y가 저장된다.
    n_set = set()   # 편의점을 방문 했다면 그 x, y가 저장된다.
    n_queue = []    # BFS 알고리즘을 위한 Queue 자료 구조
    can_go_festival = False

    # 집 주소
    house_x, house_y = map(int, sys.stdin.readline().split())
    house = (house_x, house_y)

    # n-2개의 편의점 주소 저장
    for i in range(n):
        store_x, store_y = map(int, sys.stdin.readline().split())
        store_list.append((store_x, store_y))

    # 축제 주소
    festival_x, festival_y = map(int, sys.stdin.readline().split())

    # 초기값 설정
    n_queue.append(house)
    n_set.add(house)
    while len(n_queue) > 0:

        # queue에서 현재 값을 받아 온다.
        now_position = n_queue.pop(0)
        now_position_x, now_position_y = now_position

        # 축제에 바로 갈 수 있는 경우
        if abs(now_position_x - festival_x) + abs(now_position_y - festival_y) <= 1000:
            can_go_festival = True
            break

        # 1,000안에 방문 가능한 편의점 탐색
        for store in store_list:

            # 방문 한적 없는 경우에
            if store not in n_set:
                store_x, store_y = store

                # 1,000 미터 안에 있는 경우
                if abs(now_position_x - store_x) + abs(now_position_y - store_y) <= 1000:
                    n_queue.append((store_x, store_y))
                    n_set.add((store_x, store_y))

    if can_go_festival:
        print("happy")
    else:
        print("sad")