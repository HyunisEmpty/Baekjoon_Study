import sys

n, k = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
n_dic = dict()
start = 0
end = 0
n_dic[n_list[end]] = 1   # 딕셔너리의 초깃값 설정
max_len = -1

while end < len(n_list):    # 종료조건 : 포인터가 리스트 인덱스 범위를 넘어간 경우.

    if n_dic[n_list[end]] > k:  # 딕셔너리의 현재값이 K개를 초과하는 경우
        n_dic[n_list[start]] -= 1
        # if start == end:   start와 end가 같을때 K를 초과할 수 없음
        #     end += 1
        start += 1
    else:   # 딕셔너리의 현재값이 K개 이하인 경우

        # 부분 배열의 원소의 개수가 K개 이하인 곳
        if end - start + 1 > max_len:
            max_len = end - start + 1

        end += 1
        if end != len(n_list):
            if n_list[end] in n_dic.keys():
                n_dic[n_list[end]] += 1
            else:
                n_dic[n_list[end]] = 1

print(max_len)