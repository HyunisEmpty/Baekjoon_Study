import sys

n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

start = 0
end = sum(n_list)
cutter = 0

while start <= end:

    cutter = (start + end) // 2
    cutter_tree = 0

    for tree in n_list:
        if tree > cutter:
            cutter_tree += tree - cutter

    # 자른 나무의 길이가 m보다 클때, 절단기 높이를 높여야 한다.
    if cutter_tree > m:
        start = cutter + 1
    # 자른 나무의 길이가 m보다 작을때, 절단기 높이를 낮춰야 한다.
    elif cutter_tree < m:
        end = cutter - 1
    else:
        break

# 범위 내에 정확히 m이 되는 절단기가 없는 경우에, 이진 탐색 도중 cutter_tree가 m보다 작을때의 cutter가 이진 탐색의 결과가 되는 경우가 발생한다.
if cutter_tree < m:
    cutter -= 1

print(cutter)