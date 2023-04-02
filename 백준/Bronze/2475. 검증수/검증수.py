import sys

number_list = list(map(int, sys.stdin.readline().split()))

all_sum = 0
for number in number_list:
    all_sum += number * number

print(all_sum%10)