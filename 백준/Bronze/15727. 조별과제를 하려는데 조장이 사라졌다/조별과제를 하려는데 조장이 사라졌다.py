import sys
answer = 0
n = int(sys.stdin.readline().strip())

answer += n // 5
n = n % 5
answer += n // 4
n = n % 4
answer += n // 3
n = n % 3
answer += n // 2
n = n % 2
answer += n

print(answer)