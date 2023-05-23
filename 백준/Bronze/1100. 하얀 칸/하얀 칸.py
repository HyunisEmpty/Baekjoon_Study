import sys

counter = 0
for i in range(1, 9):
    string = sys.stdin.readline().strip()
    for j in range(8):
        if i % 2 == 1 and j % 2 == 0 and string[j] == "F":
            counter += 1
        if i % 2 == 0 and j % 2 == 1 and string[j] == "F":
            counter += 1


print(counter)
