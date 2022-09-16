import sys

x, y, w, h = map(int, sys.stdin.readline().split())

w -= x
h -= y

a = [x,y,w,h]
min = a[0]

for i in a: 
    if i < min:
        min = i
        
print(min)