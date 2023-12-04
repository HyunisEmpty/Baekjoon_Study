import  sys

n, k = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
min_len = n + 1

n_dict = {1 : 0, 2 : 0}    # 1 : Ryan, 2 : Apeach
n_dict[n_list[end]] += 1

while end < len(n_list):

    # 부분 배열 안에 라이언 인형이 K개 일때, 현재 길이 최소값과 비교 및 포인터 한 칸 이동.
    if n_dict[1] == k:

        if min_len > end - start + 1:
            min_len = end - start + 1

        # start 포인터가 가리키는 인형의 개수를 카운트 하지 않는다.
        n_dict[n_list[start]] -= 1
        start += 1

    # 부분 배열 안에 라이언 인형이 K개가 아닐때
    else:

        end += 1
        if end != n:
            n_dict[n_list[end]] += 1

if min_len == n + 1:
    print(-1)
else:
    print(min_len)