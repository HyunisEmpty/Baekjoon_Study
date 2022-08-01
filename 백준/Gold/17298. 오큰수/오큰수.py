from _collections import deque
import sys

sequence_size = int(sys.stdin.readline())
stack= []
sequence_deque = deque()
sequence_deque = list(map(int, sys.stdin.readline().split(" ")))

for count_1 in range(0,len(sequence_deque)):
    if count_1 != 0:
        if sequence_deque[count_1 - 1] < sequence_deque[count_1]:
            while stack:
                count_2 = stack[-1]
                if sequence_deque[count_1] > sequence_deque[count_2]:
                    sequence_deque[count_2] = sequence_deque[count_1]
                    stack.pop()
                else:
                    break
    stack.append(count_1)

for count_1 in stack:
    sequence_deque[count_1] = -1

print(*sequence_deque)