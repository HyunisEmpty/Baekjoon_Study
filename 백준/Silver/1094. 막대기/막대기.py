import sys

target = int(sys.stdin.readline().strip())
target_list = [64, 32, 16, 8, 4, 2, 1]
number = 0

counter = 0
while number != target:

    for count in target_list:
        if target >= number + count:
            counter += 1
            number += count

print(counter)