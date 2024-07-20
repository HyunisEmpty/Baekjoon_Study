import sys

m, n = map(int, sys.stdin.readline().split())

# Sieve of Eratos
n_bool = [True for _ in range(n + 1)]
n_bool[0] = False   # 0은 소수 판별에서 제외
n_bool[1] = False   # 0은 소수 판별에서 제외
index = 2

# n_bool의 모든 원소에 한번씩 접근
while index ** 2 <= n:

    cnt = 2

    # 현재 값의 배수를 제거
    if n_bool[index]:

        while index * cnt <= n:
            n_bool[index * cnt] = False
            cnt += 1

    index += 1

for i in range(len(n_bool)):
    if n_bool[i] and i >= m:
        print(i)