import sys

n = int(sys.stdin.readline().strip())
number_list = set(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline().strip())
card_list = list(map(int, sys.stdin.readline().split()))

answer_list = []
for card in card_list:
    if card in number_list:
        answer_list.append("1")
    else:
        answer_list.append("0")

print(" ".join(answer_list))