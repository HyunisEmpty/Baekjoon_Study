import sys

n = int(sys.stdin.readline().strip())

a = 1
b = 2

for _ in range(n - 2):

    c = a + b
    a = b
    b = c

if n == 1:
    print(1)
else: 
    print(b % 10007)    