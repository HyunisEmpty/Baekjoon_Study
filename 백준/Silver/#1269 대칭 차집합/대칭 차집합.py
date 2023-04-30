import sys

a, b = map(int, sys.stdin.readline().split())

a_set = set(map(int, sys.stdin.readline().split()))
b_set = set(map(int, sys.stdin.readline().split()))

a_and_b = a_set & b_set

print(len(a_set - a_and_b) + len(b_set - a_and_b))
