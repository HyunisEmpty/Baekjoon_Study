import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().split()))
n_set = set()
start = 0
end = 0
past_end = -1 # 초기값이 -1 인 이유는 0을 가리키는 이전 최장 부분 배열이 존재 했다는 의미 이므로 의도 하지 않은 의미로서 past_end == end - 1이 될 수 있습니다.
answer = 0
while end < len(n_list):

    # end가 가리키는 값이 집합 안에 있는 경우,  현재 부분 배열의 길이가 최대임을 의미 한다.
    if n_list[end] in n_set:

        if past_end == end - 1:

            n_set.remove(n_list[start])
            start += 1

        else:

            answer += ((end - start + 1) * (end - start)) / 2

            # 이전 최장 부분배열과 중첩 되는 부분 제거하는 연산 또한 필요하다.
            if past_end - start + 1 > 0:
                answer -= ((past_end - start + 2) * (past_end - start + 1)) / 2

            past_end = end - 1

    # end가 가리키는 값이 집합 안에 없는 경우
    else:

        n_set.add(n_list[end])
        end += 1

        if end == len(n_list):

            answer += ((end - start + 1) * (end - start)) / 2

            # 이전 최장 부분배열과 중첩 되는 부분 제거하는 연산 또한 필요하다.
            if past_end - start + 1 > 0:
                answer -= ((past_end - start + 2) * (past_end - start + 1)) / 2

print(int(answer))