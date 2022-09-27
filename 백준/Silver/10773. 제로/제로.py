import sys

counter = int(sys.stdin.readline().strip())

number_list = []
for count in range(counter):
    target = int(sys.stdin.readline().strip())
    if target != 0:
        number_list.append(target)
    else:
        del number_list[len(number_list)-1]

all_sum = 0
for count in number_list:
    all_sum += count
print(all_sum)