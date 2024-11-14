import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    n = int(sys.stdin.readline().strip())
    n_list = []

    for _ in range(n):
        document, interview = map(int, sys.stdin.readline().strip().split())
        n_list.append((document, interview))

    n_list.sort()

    cnt = 1
    min_interview = n_list[0][1]

    for i in range(1, len(n_list)):

        interview = n_list[i][1]
        
        if interview < min_interview:
            min_interview = interview
            cnt += 1

        if interview == 1:
            break

    print(cnt)