import sys

# 매개변수로 배열의 시작 인덱스와 마지막 인덱스를 받는다.
def MergeSort(left_index, right_index):

    if left_index == right_index:
        return

    middle_index = (left_index + right_index) // 2  # 중간 지점 인덱스

    MergeSort(left_index, middle_index)             # 중간을 기준으로 나눈 왼쪽 리스트
    MergeSort(middle_index + 1, right_index)        # 중간을 기준으로 나눈 오른족 리스트
    Merge(left_index, middle_index, right_index)

# left_index 부터 right_index 까지 정렬 시키는 함수
def Merge(left_index, middle_index, right_index):

    global N_list

    tmp = []
    idx1 = left_index           # 왼쪽 리스트 시작 부분 인덱스
    idx2 = middle_index + 1     # 오른쪽 리스트 시작 부분 인덱스

    while idx1 <= middle_index and idx2 <= right_index:

        if N_list[idx1] < N_list[idx2]:     # 왼쪽 리스트가 더 작은 경우 tmp에 추가
            tmp.append(N_list[idx1])
            idx1 += 1
        else:                               # 오른쪽 리스트가 더 작은 경우 tmp에 추가
            tmp.append(N_list[idx2])
            idx2 += 1

    # 왼쪽 리스트에 추가 되지 못한 값이 남아 있다면 추가
    while idx1 <= middle_index:
        tmp.append(N_list[idx1])
        idx1 += 1

    # 오른쪽 리스트에 추가 되지 못한 값이 남아 있다면 추가
    while idx2 <= right_index:
        tmp.append(N_list[idx2])
        idx2 += 1

    # tmp의 결과를 N_list에 반영
    for i in range(left_index, right_index + 1):
        N_list[i] = tmp[i - left_index]

        # K 번째로 저장 되는 수
        answer_list.append(tmp[i - left_index])

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())  # 5 7
    N_list = list(map(int, sys.stdin.readline().split()))  # 4 5 1 3 2
    answer_list = []

    MergeSort(0, len(N_list) - 1)

    if len(answer_list) >= K:
        print(answer_list[K - 1])
    else:
        print(-1)

