number = int(input())
another = 0
a_1 = 1
a_2 = 1

for count in range(number-2):
    another = a_2 + a_1
    a_1 = a_2
    a_2 = another

print(a_2)