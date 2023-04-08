import sys

n = int(sys.stdin.readline().strip())

asia_dic = {}
asia_counter = {}
score_list = []
for i in range(n):
    national_number, student_number, score = map(int, sys.stdin.readline().split())
    asia_dic[score] = [national_number, student_number]

    if national_number not in asia_counter:
        asia_counter[national_number] = 0

    score_list.append(score)

score_list.sort(reverse=True)

exit_counter = 0
for score in score_list:
    national_number, student_number = asia_dic[score][0], asia_dic[score][1]

    if asia_counter[national_number] < 2:
        print(national_number, student_number)
        asia_counter[national_number] += 1
        exit_counter += 1

    if exit_counter == 3:
        break
