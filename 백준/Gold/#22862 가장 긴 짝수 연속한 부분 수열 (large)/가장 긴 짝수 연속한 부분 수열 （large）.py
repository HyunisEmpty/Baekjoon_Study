import sys

n, k = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
start = 0
end = 0
max_length = 0
k_count = 0

while end < len(n_list):

    # end 포인터가 가리키는 인덱스의 값이 짝수인 경우
    if n_list[end] % 2 == 0:
        # 짝수가 추가 되었을 때만 길이가 늘어나므로 end가 짝수인 경우일 때만 최대 길이를 확인하는 연산을 한다.
        if max_length < (end - start + 1) - k_count:
            max_length = (end - start + 1) - k_count
        end += 1
    # end 포인터가 가리키는 인덱스의 값이 홀수인 경우
    else:
        # 부분 배열 내부에 제거된 홀수의 수가 k개인 경우 (새로운 홀수를 제거하기 위해서는 start가 가장 먼저 만나는 k를 제거 해야한다.)
        if k_count == k:
            if n_list[start] % 2 == 1:
                k_count -= 1
            start += 1
        else:
            k_count += 1
            end += 1

print(max_length)