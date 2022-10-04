import sys

case_count = int(sys.stdin.readline().strip())
for test_count in range(case_count):
    one = [0, 1]
    zero = [1, 0]

    number = int(sys.stdin.readline().strip())

    if number >= 2:
        for count in range(1, number):  # n이 2인경
            one.append(one[len(one) - 1] + one[len(one) - 2])
            zero.append(zero[len(zero) - 1] + zero[len(zero) - 2])

    print(zero[number], one[number])