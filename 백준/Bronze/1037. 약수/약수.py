import sys

number = int(sys.stdin.readline().strip())

number_list = list(map(int, sys.stdin.readline().split()))
number_list.sort(reverse=True)

if number % 2 == 0:
    print(number_list[0] * number_list[-1])
else:
    number = int(((number-1)/2))
    print(number_list[number] * number_list[number])