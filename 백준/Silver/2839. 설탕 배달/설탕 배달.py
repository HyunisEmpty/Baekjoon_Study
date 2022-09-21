import sys

sugar_weight = int(sys.stdin.readline().strip())

# 5배수가 아니라면 3을 뺀다.
# 5의 배수라면 5로 나눈 몫을 구한다.

count = 0
while not (sugar_weight < 3):
    # 5로 나누어 떨어지지 않는다면
    if (sugar_weight % 5) != 0 :
        # sugar_weight 에서 3을 빼고 count 에 1을 더한다
        sugar_weight -= 3
        count += 1
    # 5로 나누어 떨어진다면
    else:
        # sugar_weight 을 5로 나눈 몫을 count 에 추가 한다.
        count += sugar_weight // 5
        sugar_weight -= sugar_weight

if sugar_weight == 0:
    print(count)
else:
    print(-1)