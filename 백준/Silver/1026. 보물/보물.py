import sys

num = int(sys.stdin.readline())

data1 = list(map(int, sys.stdin.readline().split()))
data2 = list(map(int, sys.stdin.readline().split()))

data1.sort(reverse = False)
data2.sort(reverse = True)

data_sum = 0
for count in range(num):
    data_sum += data1[count] * data2[count]

print(data_sum)