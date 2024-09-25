import sys

n, m, r = map(int, sys.stdin.readline().split())
# 인접 리스트 정의
n_list = [[] for i in range(n + 1)]
# 방문 순서 저장
n_counted = [0] * (n + 1)
# DFS 스택 정의
stack = []

# 노드의 연결 관계 저장
for i in range(m):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    # 상호 연결관계 저장
    n_list[node_1].append(node_2)
    n_list[node_2].append(node_1)

# 각 노드의 연결 리스트를 내림차순으로 정렬 (스택을 사용하기 때문)
for i in range(1, n + 1):
    n_list[i].sort(reverse=True)

# DFS 초기값 설정
stack.append(r)
count = 0  # 방문 순서 카운트

while stack:
    now_node = stack.pop()

    # 현재 노드를 방문한 적 없다면 방문 순서 기록
    if n_counted[now_node] == 0:
        count += 1
        n_counted[now_node] = count

        # 이웃 노드를 스택에 추가
        for neighbor_node in n_list[now_node]:
            if n_counted[neighbor_node] == 0:  # 아직 방문하지 않은 노드만 추가
                stack.append(neighbor_node)

for i in range(len(n_counted)):

    if i != 0:
        print(n_counted[i])
