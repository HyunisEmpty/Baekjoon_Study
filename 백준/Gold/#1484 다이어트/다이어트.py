import sys

n = int(sys.stdin.readline().strip())

now_weight = 2
past_weight = 1
answer_list = []

while True:

    g = (now_weight * now_weight) - (past_weight * past_weight)

    if now_weight - past_weight == 1 and g > n:
        break

    if g > n:
        past_weight += 1
    elif g == n:
        answer_list.append(now_weight)
        now_weight += 1
    elif g < n:
        now_weight += 1

if len(answer_list) == 0:
    print(-1)
else:
    for ans in answer_list:
        print(ans)
