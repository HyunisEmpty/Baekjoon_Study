from collections import deque

number = int(input())
data_deque = deque()

for count in range(1,number+1):
    data_deque.append(count)

while len(data_deque) != 1:
    data_deque.popleft()
    data_deque.append(data_deque[0])
    data_deque.popleft()

print(data_deque[0])