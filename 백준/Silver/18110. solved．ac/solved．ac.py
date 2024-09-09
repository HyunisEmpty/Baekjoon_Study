import sys

n = int(sys.stdin.readline().strip())
n_list = sorted([int(sys.stdin.readline().strip()) for i in range(n)])
n_sum = sum(n_list)

def Round(number):

    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)

# 반올림한 절사값
truncation = Round(n * 0.15)

# 전체 난이도에서 절사값 제외
for i in range(truncation):
    n_sum -= n_list[i]
    n_sum -= n_list[-(i+1)]

if n == 0:
    print(0)
else:
    print(Round(n_sum/(n - truncation * 2)))