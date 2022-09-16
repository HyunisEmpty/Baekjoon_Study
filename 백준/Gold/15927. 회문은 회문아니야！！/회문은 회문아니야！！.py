import sys

def Palindrome(string):
    line_1 = string
    line_2 = string[::-1]

    flag_1 = 0
    for count in range(len(string)):
        if line_1[count] == line_2[count]:
            flag_1 += 1

    # 펠린드롬 경우
    if flag_1 == len(string):

        first_word = string[0]
        flag_2 = 0
        for count in range(len(string)):
            if string[count] == first_word:
                flag_2 += 1

        if flag_2 == len(string):
            return 0
        else:
            return 1
    # 펠린드롬이아닌 경우
    else:
        return 2

carrier = sys.stdin.readline().strip()
flag = Palindrome(carrier)

if flag == 0:
    print(-1)
if flag == 1:
    print(len(carrier)-1)
if flag == 2:
    print(len(carrier))