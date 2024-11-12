import sys
import heapq

n = int(sys.stdin.readline().strip())   # 사람의 수
n_list = []                             # 사람의 집과 오피스 정보 리스트
for _ in range(n):
    a, b = sorted(map(int, sys.stdin.readline().strip().split()))
    n_list.append((a, b))
d = int(sys.stdin.readline().strip())   # 선분의 길이
n_list.sort()                           # a를 기준으로 정렬

# print(n_list)

min_heap1 = []
min_heap2 = []
max_len = 0
right = 0
for left in range(len(n_list)):         # left 포인터 기준

    if right < left:
        right += 1

    a, b = n_list[left]                 # 현재 포인터가 지칭하는 값을 받아옴

    while right != len(n_list):

        am, bm = n_list[right]

        if a + d > am:  # ai + d > am(am≥ai) : am(시작점)이 선분에 포함되는 경우
            if a + d >= bm:    # ai + d ≥ bm : (am, bm)이 선분에 포함되는 경우
                heapq.heappush(min_heap1, (am, bm))
            else:                           # ai + d < bm : bm 만 선분에 포함 안되는 경우
                heapq.heappush(min_heap2, (bm, am))
            right += 1
        else:
            break

    while len(min_heap2) != 0 and a + d >= min_heap2[0][0]: # 이제는 bm이 선분에 포함되는 경우가 있는지 확인 확인
        bm, am = heapq.heappop(min_heap2)
        if am >= a:
            heapq.heappush(min_heap1, (am, bm))

    while len(min_heap1) != 0 and a > min_heap1[0][0]:
        heapq.heappop(min_heap1)

    # print("now left point index :", left, n_list[left][0], a + d)
    # print("now right point index :", right)
    # print("am만 선분에 포함되는 튜플 :", min_heap2)
    # print("선분에 포함되는 튜플 :", min_heap1)

    max_len = max(max_len, len(min_heap1))
    # print(max_len)

print(max_len)