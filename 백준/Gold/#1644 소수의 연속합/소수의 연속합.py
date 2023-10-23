import sys

def Eratos(n):
    n_bool = [True for _ in range(n)]
    n_bool[0] = False
    n_index = 1

    # 현재 값이 True라면 그 배수값들을 False로 변경, 루트 n보다 작은 값까지 반복
    while (n_index + 1) ** 2 <= n:
        if n_bool[n_index]:
            cnt = 2
            while (n_index + 1) * cnt <= n:
                n_bool[((n_index + 1) * cnt) - 1] = False
                cnt += 1
        n_index += 1
    n_list = []

    # n_bool 안에서 True, 즉 소수인 값만 n_list에 추가한다.
    for i in range(len(n_bool)):
        if n_bool[i]:
            n_list.append(i + 1)

    return n_list

N = int(sys.stdin.readline().strip())

prime_list = Eratos(N)
answer = 0

for start in range(len(prime_list)):
    n_sum = prime_list[start]

    if n_sum == N:
        answer += 1
        break
    elif n_sum > N:
        break

    for end in range(start + 1, len(prime_list)):
        n_sum += prime_list[end]

        if n_sum == N:
            answer += 1
            break
        elif n_sum > N:
            break


print(answer)