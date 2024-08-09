import sys

n_list = list(map(int, sys.stdin.readline().strip().split()))
da_list = [1, 2, 3, 4, 5, 6, 7, 8]

if n_list == da_list:
    print("ascending")
elif n_list == da_list[::-1]:
    print("descending")
else:
    print("mixed")