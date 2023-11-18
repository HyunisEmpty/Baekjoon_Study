import sys

n, d, k, c = map(int, sys.stdin.readline().split())
n_list = []

for i in range(n):
    n_list.append(int(sys.stdin.readline().strip()))

for i in range(k-1):
    n_list.append(n_list[i])

n_set = set()
n_set.add(c)
start = 0
end = k-1

for i in range(k):
    n_set.add(n_list[i])
max_len = -1

while end < len(n_list):


    if max_len < len(n_set):
        max_len = len(n_set)

    if n_list[start] in n_set and n_list[start] != c and n_list[start] not in n_list[start+1:end+1]:
        n_set.remove(n_list[start])
    start += 1
    end += 1
    if end != len(n_list):
        n_set.add(n_list[end])

print(max_len)