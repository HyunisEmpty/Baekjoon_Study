import sys
from collections import deque

s_l = list(sys.stdin.readline().strip())
t_l = list(sys.stdin.readline().strip())
s = deque(s_l)
t = deque(t_l)

reverse = False
while len(t) != len(s):

    if reverse == False:
        last_word = t.pop()
    else:
        last_word = t.popleft()

    if last_word == "B":
        reverse = not reverse

s = list(s)
t = list(t)

if reverse:
    if s == t[::-1]:
        print(1)
    else:
        print(0)
else:
    if s == t:
        print(1)
    else:
        print(0)