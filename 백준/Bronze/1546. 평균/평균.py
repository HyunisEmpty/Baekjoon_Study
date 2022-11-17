import sys

number = int(sys.stdin.readline().strip())
number_list = list(map(int, sys.stdin.readline().split()))
max_ = max(number_list)
sum_ = 0
for count in range(number):
    sum_ += number_list[count]/max_ * 100

print(sum_/number)