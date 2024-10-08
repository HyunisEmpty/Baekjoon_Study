import sys
from collections import deque

test = int(sys.stdin.readline().strip())
for test_case in range(test):

    set1 = set()
    set2 = set()

    v, e = map(int, sys.stdin.readline().strip().split())    # 노드와 간선 입력
    v_list = [[] for _ in range(v + 1)]
    visited = [False for _ in range(v + 1)]
    queue = deque()

    for i in range(e):  # 간선 정보 저장
        v1, v2 = map(int, sys.stdin.readline().strip().split())
        v_list[v1].append(v2)
        v_list[v2].append(v1)

    for vertex in range(1, len(v_list)):

        if visited[vertex] == False:    # 방문한적 없는 경우
            set1.add(vertex)
            queue.append((vertex, 1))

            while queue:

                vertex_now, set_number = queue.popleft()
                visited[vertex_now] = True  # 현재 노드를 방문 했다고 확인

                for neighbor in v_list[vertex_now]: # 현재 노드의 이웃 노드에 접근

                    if visited[neighbor] == False:  # 이웃 노드를 방문 안한 경우
                        if set_number == 1: # 현재 노드가 1번 집합에 있는 경우
                            set2.add(neighbor)
                            queue.append((neighbor, 2))
                        elif set_number == 2: # 현재 노드가 1번 집합에 있는 경우
                            set1.add(neighbor)
                            queue.append((neighbor, 1))

    flag = False
    for vertex in set1:
        if vertex in set2:
            flag = True

    if flag:
        print("NO")
    else:
        print("YES")

