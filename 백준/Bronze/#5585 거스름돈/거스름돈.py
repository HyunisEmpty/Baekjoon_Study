import sys

coins = 1000 - int(sys.stdin.readline().strip())

count = 0
while coins != 0:
    if coins >= 500:
        coins -= 500
        count += 1
    elif coins >= 100:
        coins -= 100
        count += 1
    elif coins >= 50:
        coins -= 50
        count += 1
    elif coins >= 10:
        coins -= 10
        count += 1
    elif coins >= 5:
        coins -= 5
        count += 1
    elif coins >= 1:
        coins -= 1
        count += 1

print(count)