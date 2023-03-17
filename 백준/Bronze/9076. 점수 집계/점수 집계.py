import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    score_list = list(map(int, sys.stdin.readline().split()))

    # 선택 정렬
    for i in range(4):
        min_index = i
        for j in range(i+1, 5):
            if score_list[j] < score_list[min_index]:
                min_index = j
        score_list[i], score_list[min_index] = score_list[min_index], score_list[i]

    if(score_list[3] - score_list[1]) >= 4:
        print("KIN")
    else:
        print(score_list[1] + score_list[2] + score_list[3])