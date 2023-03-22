import sys

# 그리디 알고리즘

formula_list = sys.stdin.readline().strip()
formula_list = formula_list.split("-")
number_list = []

index = 0
all_sum = 0
for formula in formula_list:
    number_list = formula.split("+")
    number_sum = 0
    for number in number_list:
        number_sum += int(number)

    if index == 0:
        all_sum += number_sum
    else:
        all_sum -= number_sum
    index += 1

print(all_sum)