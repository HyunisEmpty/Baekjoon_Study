import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    """
    n : 서로다른 정수의 개수 
    k : 목표값 
    n_list : 서로다른 정수가 주어지는 리스트 
    left : 왼쪽 포인터 
    right : 오른쪽 포인터 
    app : 근사값(approximation)
    min_error : 오차가 최소인 경우 
    min_error_count : 오차가 최소인 경우의 수
    """

    n, k = map(int, sys.stdin.readline().split())
    n_list = sorted(list(map(int, sys.stdin.readline().strip().split())))

    left = 0
    right = len(n_list) - 1

    min_error = -1
    min_error_count = 0

    while left < right:

        lr = n_list[left] + n_list[right]
        error = abs(k - lr)

        if min_error != -1:
            if error < min_error:
                min_error = error
                min_error_count = 1
            elif error == min_error:
                min_error_count += 1
        else:
            min_error = error
            min_error_count = 1

        # 근사값이 k보다 큰 경우
        if lr > k:
            right -= 1
        # 근사값이 k보다 작은 경우
        else:
            left += 1

    print(min_error_count)