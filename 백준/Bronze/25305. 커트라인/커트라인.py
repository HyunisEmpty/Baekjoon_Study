import sys

student_number, winner = map(int, sys.stdin.readline().split())
score_list = list(map(int, sys.stdin.readline().split()))

for i in range(1, student_number):
    for j in range(i, 0, -1):
        if score_list[j-1] > score_list[j]:
            score_list[j-1], score_list[j] = score_list[j], score_list[j-1]
        else:
            break

print(score_list[student_number - winner] )