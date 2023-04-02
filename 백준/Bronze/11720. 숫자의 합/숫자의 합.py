import sys

n = int(sys.stdin.readline().strip())
number = sys.stdin.readline().strip()

all_sum = 0
for i in range(n):
    all_sum += int(number[i])

print(all_sum)