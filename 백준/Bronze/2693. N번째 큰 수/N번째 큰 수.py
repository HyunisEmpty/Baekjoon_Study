import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    number_list = list(map(int, sys.stdin.readline().split()))

    for i in range(9):

        min_index = i

        for j in range(i+1, 10):
            if number_list[j] < number_list[min_index]:
                min_index = j

        number_list[i], number_list[min_index] = number_list[min_index], number_list[i]

    print(number_list[7])