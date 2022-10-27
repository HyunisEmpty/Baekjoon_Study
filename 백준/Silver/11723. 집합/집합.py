import sys

test_case = int(sys.stdin.readline().strip())
set_list = set()
for test_count in range(test_case):
    command = list(sys.stdin.readline().split())

    if command[0] == "add":
        if command[1] in set_list:
            pass
        else:
            set_list.add(command[1])

    elif command[0] == "remove":
        if command[1] in set_list:
            set_list.discard(command[1])
        else:
            pass

    elif command[0] == "check":
        if command[1] in set_list:
            print(1)
        else:
            print(0)

    elif command[0] == "toggle":
        if command[1] in set_list:
            set_list.discard(command[1])
        else:
            set_list.add(command[1])

    elif command[0] == "all":
        set_list = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}

    elif command[0] == "empty":
        set_list.clear()