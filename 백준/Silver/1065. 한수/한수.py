import sys

number = int(sys.stdin.readline().strip())

counter = 99
if number < 100:
    print(number)
elif number == 1000:
    print(144)
else:
    for count in range(100, number + 1):
        t1 = count // 100
        count -= t1 * 100
        t2 = count // 10
        count -= t2 * 10
        t3 = count

        if t1 - t2 == t2 - t3:
            counter += 1

    print(counter)
