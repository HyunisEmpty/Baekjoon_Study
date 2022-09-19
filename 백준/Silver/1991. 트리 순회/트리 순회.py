import sys

node = int(sys.stdin.readline().strip())

tree = []
for count in range(node):
    tree.append(list(map(str, sys.stdin.readline().split())))

def Left(list):
    fifo_list = []
    fifo_list.append(list[0][0])
    fifo_str = ""

    while len(fifo_list) != 0:

        target = fifo_list[0]
        fifo_str += str(target)
        del fifo_list[0]

        for count in range(len(list)):
            if list[count][0] == target:
                if list[count][2] != ".":
                    fifo_list.insert(0, list[count][2])
                if list[count][1] != ".":
                    fifo_list.insert(0, list[count][1])

    return fifo_str


def Mid(list):

    mifo_list = []
    mifo_list.append(list[0][0])

    while len(mifo_list) != len(list):

        for count_1 in range(len(list)):
            target = list[count_1][0]

            for count_2 in range(len(mifo_list)):
                if mifo_list[count_2] == target:
                    if list[count_1][2] != ".":
                        mifo_list.insert(count_2 + 1, list[count_1][2])
                    if list[count_1][1] != ".":
                        mifo_list.insert(count_2, list[count_1][1])
                    break

    return mifo_list


def Last(list):
    lifo_list = []
    lifo_list.append(list[0][0])
    lifo_str = ""

    while len(lifo_list) != 0:

        target = lifo_list[0]
        lifo_str = target + lifo_str
        del lifo_list[0]

        for count in range(len(list)):
            if list[count][0] == target:
                if list[count][1] != ".":
                    lifo_list.insert(0, list[count][1])
                if list[count][2] != ".":
                    lifo_list.insert(0, list[count][2])

    return lifo_str

first = Left(tree)
mid = Mid(tree)
last = Last(tree)
print(first)
k = ""
for x in mid:
    k += x
print(k)
print(last)