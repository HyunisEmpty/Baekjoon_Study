import sys

n = int(sys.stdin.readline().strip())
loop_list = []

for i in range(n):
    loop_list.append(int(sys.stdin.readline().strip()))

# 로프 내림차순으로 정렬
loop_list.sort(reverse=True)

# 그리디 알고리즘
max_weight = 0
for i in range(n):
    if i == 0:
        max_weight = loop_list[i]
    else:
        if loop_list[i] * (i + 1) >= max_weight:
            max_weight = loop_list[i] * (i + 1)

print(max_weight)