import sys

command_count = int(sys.stdin.readline().strip())
stack = []

for count in range(command_count):
    command_list = list(map(str, sys.stdin.readline().split()))

    if command_list[0] == "push":
        stack.append(int(command_list[1]))

    if command_list[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
            del stack[len(stack)-1]

    if command_list[0] == "size":
        print(len(stack))

    if command_list[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if command_list[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])

    command_list = []
    # print("stack :", stack)

