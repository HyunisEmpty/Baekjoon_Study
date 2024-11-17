import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

n_list = [[] for _ in range(n)]

queue = deque()

for i in range(n):
    input_list = list(map(int, sys.stdin.readline().strip().split()))

    for j in range(len(input_list)):

        if i == j:
            pass
        else:
            if input_list[j] == 1:
                n_list[i].append(j)

travel = list(map(int, sys.stdin.readline().strip().split())) # 연결된 도시를 도시별 인덱스로 표현

visited_city = set()
queue.append(travel[0]-1)
visited_city.add(travel[0]-1)
while queue:

    city = queue.popleft()

    for neighbor_city in n_list[city]:
        if neighbor_city not in visited_city:
            visited_city.add(neighbor_city)
            queue.append(neighbor_city)

flag = True

for city in travel:
    if city-1 not in visited_city:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")