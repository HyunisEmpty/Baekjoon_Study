import sys

computer_size = int(sys.stdin.readline())
case = int(sys.stdin.readline())

computer_line = []
for count in range(computer_size+1):
    computer_line.append([])
computer_line[0].append(computer_size)

for count in range(case):
    main_computer, sub_computer = map(int, sys.stdin.readline().split(" "))
    computer_line[main_computer].append(sub_computer)
    computer_line[sub_computer].append(main_computer)
    #[[7], [2, 5], [3], [], [7], [2, 6], [], []]

last_list = computer_line[1]
Access = [1]

while last_list: #리스트안에 뭔가있으면 true 없으면 false

    count_1 = last_list[0]
    if count_1 in Access:
        pass
    else:
        Access.append(count_1)
    for count_2 in computer_line[count_1]:
        if count_2 in Access:
            pass
        else:
            last_list.append(count_2)

    last_list.pop(0)
print(len(Access)-1)