import sys
import random
sys.setrecursionlimit(10**6)    # RecursionError 예방

n = int(sys.stdin.readline().strip())
number_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
random.shuffle(number_list) # 최악의 경우(리스트가 정렬된 경우)를 대비한 리스트를 섞습니다.

def quick_sort(arr, left, right):
    if left < right:  # 조건문에 들어오지 못하는 경우는 배열의 크기가 1인경우 뿐이다.

        pivot_index = partition(arr, left, right)

        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)


def partition(arr, left, right):
    # 피봇을 리스트에 가장 오른쪽에 있는 값으로 선정한다.
    pivot = arr[right]
    # i 는 리스트안에서 pivot보다 작은 원소의 개수이다.
    i = left - 1

    for j in range(left, right):

        # 피봇보다 작은 경우 if문 안으로 큰경우 무시하고 j값이 증가한다.
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    # 리스트 가장 끝에 있던 피봇을 자기보다 작은 값들의 가장 오른쪽에 오도록한다.
    arr[i + 1], arr[right] = arr[right], arr[i+1]

    # 현재 피봇의 위치를 출력
    return i + 1


quick_sort(number_list, 0, len(number_list)-1)

for number in number_list:
    print(number)