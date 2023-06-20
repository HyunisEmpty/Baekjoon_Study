import sys

default_len, new_score, limit_len = map(int, sys.stdin.readline().split())


def FindScore(target_list):
    count = 0

    for number in target_list:
        count += 1
        if number == new_score:
            break

    return count

number_list = []
if default_len != 0:
    number_list = list(map(int, sys.stdin.readline().split()))

    # 혹시 모르니 내림차순으로 재 정렬
    number_list.sort(reverse=True)

answer = ""
if default_len == limit_len:
    if number_list[len(number_list) - 1] >= new_score:
        answer = "-1"
    else:
        number_list[len(number_list) - 1] = new_score
        number_list.sort(reverse=True)
        answer = FindScore(number_list)
else:
    number_list.append(new_score)
    number_list.sort(reverse=True)
    answer = FindScore(number_list)

print(answer)