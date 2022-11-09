import sys
number_list = sorted(sys.stdin.readline().strip())
number_list = number_list[::-1]

word = ""
for count in range(len(number_list)):
    word += number_list[count]

print(word)