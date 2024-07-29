import sys

n1, n2 = map(int, sys.stdin.readline().split())

# 최대 공약수
greatest_divisor = 0

cnt = 1

while cnt <= n1 and cnt <= n2:

    if n1%cnt == 0 and n2%cnt == 0:
        greatest_divisor = cnt

    cnt += 1
print(greatest_divisor)

# 최소 공약수
smallest_divisor = 0
car1 = n1
car2 = n2

while smallest_divisor == 0:

    if car1 > car2:
        car2 += n2
    elif car2 > car1:
        car1 += n1
    else:
        smallest_divisor += car1

print(smallest_divisor)