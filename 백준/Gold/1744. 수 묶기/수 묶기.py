import sys

number_count = int(sys.stdin.readline().strip())
number_list_negative = []
number_list_positive = []
number_zero_flag = False

for count in range(number_count):
    number = int(sys.stdin.readline().strip())
    if number > 0:
        number_list_positive.append(number)
    if number == 0:
        number_zero_flag = True
    if number < 0:
        number_list_negative.append(number)

number_list_positive.sort(reverse=True)
number_list_negative.sort(reverse=False)

number_sum = 0
while number_list_negative != [] or number_list_positive != []:

    if len(number_list_positive) >= 2:
        p1 = number_list_positive[0]
        del number_list_positive[0]
        p2 = number_list_positive[0]
        del number_list_positive[0]
        if p1 != 1 and p2 != 1:
            number_sum += p1 * p2
        else:
            number_sum += p1 + p2
    elif len(number_list_positive) == 1:
        p3 = number_list_positive[0]
        del number_list_positive[0]
        number_sum += p3

    if len(number_list_negative) >= 2:
        n1 = number_list_negative[0]
        del number_list_negative[0]
        n2 = number_list_negative[0]
        del number_list_negative[0]
        number_sum += n1 * n2
    elif len(number_list_negative) == 1:
        n3 = number_list_negative[0]
        del number_list_negative[0]
        if number_zero_flag == True:
            number_sum += n3 * 0
        else:
            number_sum += n3

# print(number_list_positive)
# print(number_list_negative)
# print(number_zero_flag)
print(number_sum)