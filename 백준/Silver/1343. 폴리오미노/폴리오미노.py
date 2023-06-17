import sys

string_list = sys.stdin.readline().strip().split(".")

new_string = ""
for i in range(len(string_list)):
    new_string = ""
    string_len = len(string_list[i])
    # 빈칸이 아닐때
    if string_len != 0:

        quo_4 = string_len // 4
        rem_4 = string_len % 4
        quo_2 = rem_4 // 2
        rem_2 = rem_4 % 2

        new_string = ("AAAA" * quo_4) + ("BB" * quo_2) + ("X" * rem_2)

        string_list[i] = new_string


answer = ""
for i in range(len(string_list)):
    if i != len(string_list) - 1:
        answer += string_list[i] + "."
    else:
        answer += string_list[i]

count = 0
for i in range(len(answer)):
    if answer[i] == "X":
        count = 1

if count == 1:
    print(-1)
else:
    print(answer)