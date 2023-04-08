import sys

n, k = map(int, sys.stdin.readline().split())

number_list = list(map(int, sys.stdin.readline().split()))
number_list.sort()

print(number_list[k-1])