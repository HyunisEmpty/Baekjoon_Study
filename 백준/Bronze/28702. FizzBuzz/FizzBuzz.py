import sys

n_list = [ sys.stdin.readline().strip() for i in range(3)]
n_set = set([str(i) for i in range(10)])
index = 0
number = 0

for i in n_list:

    if i[0] in n_set:
        number = int(i)
        break

    index += 1

while index < 4:

    if index == 3:
        if number%3 == 0 and number%5 == 0:
            print("FizzBuzz")
        elif number%3 == 0 and number%5 != 0:
            print("Fizz")
        elif number%3 != 0 and number%5 == 0:
            print("Buzz")
        else:
            print(number)
    number += 1
    index += 1

