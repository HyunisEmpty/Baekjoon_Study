import sys

flag = True
while flag:
    number = sys.stdin.readline().strip()

    if number == "0":
        break

    if number == number[::-1]:
        print("yes")
    else:
        print("no")