import sys

answer_dic = {}
answer_list = []

n = int(sys.stdin.readline().strip())
number_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())
card_list = list(map(int, sys.stdin.readline().split()))

# number_list와 card_list의 교집합을 구한다.
card_set = set(number_list) & set(card_list)

for number in number_list:
    # 현재 가져온 숫자가 교집합에 있는경우
    if number in card_set:
        if number in answer_dic.keys():
            answer_dic[number] += 1
        else:
            answer_dic[number] = 1

for card in card_list:
    if card in answer_dic.keys():
        answer_list.append(str(answer_dic[card]))
    else:
        answer_list.append("0")

print(" ".join(answer_list))

