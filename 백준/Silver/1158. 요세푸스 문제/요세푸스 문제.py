from collections import deque
import sys

data_deque = deque()
last_deque = deque()

people, number = map(int, sys.stdin.readline().split(" "))
data_deque = deque([i+1 for i in range(people)])

number_count = 1
while data_deque:

    if number_count == number:
        last_deque.append(str(data_deque.popleft()))
        number_count = 1
    else:
        data_deque.append(str(data_deque.popleft()))
        number_count += 1

print("<"+", ".join(last_deque)+">")