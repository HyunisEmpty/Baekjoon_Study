import sys

a = 0
for i in range(5):
    c = int(sys.stdin.readline().strip())

    if c < 40:
        a += 40
    else:
        a += c 
print(int(a/5))