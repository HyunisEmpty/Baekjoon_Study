import sys
import heapq

n, l = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
min_heap = []
min_list = []
del_dic = dict()

for i in range(n):      # n개의 모든 수에 접근

    heapq.heappush(min_heap, n_list[i])        # 삽입 연산

    if i + 1 > l:
        target = n_list[i - l]
        # print("target", target)

        if target not in del_dic:
            del_dic[target] = 1
        else:
            del_dic[target] += 1

    while len(min_heap) > l and min_heap[0] in del_dic:       # 힙에 불필요한 값이 있다면

        target = heapq.heappop(min_heap)  # 제거 연산

        del_dic[target] -= 1

        if del_dic[target] == 0:
            del del_dic[target]

    min_list.append(min_heap[0])

print(*min_list)