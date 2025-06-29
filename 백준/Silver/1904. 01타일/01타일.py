import sys

n = int(sys.stdin.readline().strip())
dp_1 = 1
dp_2 = 2
dp_ans = 0

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(3, n + 1):
       dp_ans = dp_2 + dp_1
       dp_1 = dp_2%15746
       dp_2 = dp_ans%15746
    print(dp_ans%15746)