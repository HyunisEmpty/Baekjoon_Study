import sys


number_case_count, target_cost = map(int, sys.stdin.readline().split())
number_list = []
counter = 0

for count in range(number_case_count):
    carrier = int(sys.stdin.readline().strip())
    if carrier > target_cost:
        break
    else:
        number_list.append(carrier)

index = len(number_list) - 1
while target_cost != 0:
    if number_list[index] > target_cost:
        index -= 1
    else:
        share = target_cost//number_list[index]
        target_cost -= number_list[index] * share
        counter += share


print(counter)