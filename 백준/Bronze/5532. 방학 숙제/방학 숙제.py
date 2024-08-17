import sys

l = int(sys.stdin.readline().strip())
a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())
d = int(sys.stdin.readline().strip())

l_a = a//c
if a%c != 0:
    l_a += 1

l_b = b//d
if b%d != 0:
    l_b += 1

print(l - max(l_a,l_b))

