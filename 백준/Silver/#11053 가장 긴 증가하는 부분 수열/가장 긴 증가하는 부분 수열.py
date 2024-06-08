import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().strip().split()))

# 오름 차순 정렬, 중복 제거
n_set = set(n_list)
n_sort_list = sorted(list(n_set))
n_sort_list = n_sort_list[::-1]

# 각 원소의 최장 증가 부분 수열을 저장하는 리스트 생성
subsequence_list = [0 for _ in range(n)]
for sort_element in n_sort_list:

    long_subsequence = 0

    for i in range(1, n + 1):

        if sort_element == n_list[n-i]: # 비교 대상이 자신인 경우
            subsequence_list[n-i] = long_subsequence + 1
        else:
            # 가져온 값이 자신 보다 크며 자신 보다 크며, 부분 수열의 길이가 지금까지 길이 보다 길다면
            if n_list[n-i] > sort_element and long_subsequence < subsequence_list[n-i]:
                long_subsequence = subsequence_list[n-i]

print(max(subsequence_list))