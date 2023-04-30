import sys

test_count = int(sys.stdin.readline().strip())
deque = []
for test in range(test_count):

    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == "push_front":
        deque.insert(0, int(command[1]))
    if command[0] == "push_back":
        deque.append(int(command[1]))
    if command[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            del deque[0]
    if command[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])
            del deque[len(deque)-1]
    if command[0] == "size":
        print(len(deque))
    if command[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    if command[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    if command[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])