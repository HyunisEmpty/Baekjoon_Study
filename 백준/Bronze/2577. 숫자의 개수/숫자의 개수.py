import sys

abc = 1
for i in range(3):
    abc = abc * int(sys.stdin.readline().strip())
abc = str(abc)
n_list = [0] * 10


for word in abc:
    n_list[int(word)] += 1

for i in range(10):
    print(n_list[i])