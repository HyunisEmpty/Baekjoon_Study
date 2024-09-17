import sys

n = int(sys.stdin.readline().strip())
answer = 0
answer2 = 0

for i in range(1, n + 1):
    answer += i
    answer2 += i ** 3

print(answer**1)
print(answer**2)
print(answer2)
