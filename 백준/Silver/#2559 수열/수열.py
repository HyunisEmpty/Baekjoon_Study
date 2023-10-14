import sys

N, K = map(int, sys.stdin.readline().split())
day_list = list(map(int, sys.stdin.readline().split()))
day_sum = sum(day_list[0:K])
start = 0
end = K - 1
answer = day_sum

while N != end:

    if day_sum > answer:
        answer = day_sum

    day_sum -= day_list[start]
    start += 1
    end += 1
    if end != N:
        day_sum += day_list[end]

print(answer)