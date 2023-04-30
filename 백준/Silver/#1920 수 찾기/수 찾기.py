import sys

n = int(sys.stdin.readline().strip())
n_list = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())
m_list = list(map(int, sys.stdin.readline().split()))

for number in m_list:
    if number in n_list:
        print(1)
    else:
        print(0)