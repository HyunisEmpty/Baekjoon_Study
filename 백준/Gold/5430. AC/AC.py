import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    # 명령어 입력
    p = sys.stdin.readline().strip()

    # 리스트에 들어있는 수의 개수
    n = int(sys.stdin.readline().strip())

    # 리스트 입력
    n_list = sys.stdin.readline().strip('\n[]')
    if n_list == "":
        n_list = list()
    else:
        n_list = list(map(int, n_list.split(',')))

    left = 0
    right = n - 1
    # False인 경우 인덱스로 right를 사용, True인 경우 left를 사용
    reverse = False
    answer = ""

    # 명령어 실행
    for i in range(len(p)):

        # 아직 연산할 수 있는 값이 리스트에 있는 경우
        if left <= right:
            if p[i] == "R":

                reverse = not reverse

            elif p[i] == "D":

                # right 값 제거
                if reverse == False:
                    n_list[left] = -1
                    left += 1
                elif reverse == True:
                    n_list[right] = -1
                    right -= 1
        # 아직 연산할 수 있는 값이 리스트에 없는 경우
        else:
            if p[i] == "D":
                answer = "error"
            else:
                pass

    # 정답 출력
    if answer == "error":
        print(answer)
    else:
        for i in range(left, right + 1):
            # 뒤집히지 않은 상태
            if reverse == False:

                # 마지막 값이 아니라면
                if i != right:
                    answer += str(n_list[i]) + ","
                else:
                    answer += str(n_list[i])

            # 뒤집힌 상태
            if reverse == True:

                # 마지막 값이 아니라면
                if i != left:
                    answer = str(n_list[i]) + "," + answer
                else:
                    answer = str(n_list[i]) + answer


        print("["+ answer + "]")
