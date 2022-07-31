string_list = []

while True:
    input_data = input()
    if input_data == ".":
        break
    else:
        string_list.append(input_data)

for count_x_string in string_list:
    stack_list = []
    for count_x_int in range(len(count_x_string)):
        carrier = count_x_string[count_x_int]
        if (carrier == "(" or carrier == ")") or (carrier == "[" or carrier == "]"):
            stack_list.append(carrier)
        if len(stack_list) >= 2:
            if stack_list[-1] == ")" and stack_list[-2] == "(":
                stack_list.pop()
                stack_list.pop()
            elif stack_list[-1] == "]" and stack_list[-2] == "[":
                stack_list.pop()
                stack_list.pop()
    if stack_list == []:
        print("yes")
    else:
        print("no")