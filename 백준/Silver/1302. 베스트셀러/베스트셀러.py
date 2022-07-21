count_num = int(input())
book_list = []
for count_1 in range(count_num):
    string = input()
    if string in book_list:
        index_num = book_list.index(string)
        book_list[index_num + 1] = book_list[index_num + 1] + 1
    else:
        book_list.append(string)
        book_list.append(1)

max = 0
for count in range(1, len(book_list), 2):
    num = book_list[count]
    if num >= max :
        max = num

last_list = []
for count in range(1, len(book_list), 2):
    num = book_list[count]
    if num == max:
        last_list.append(book_list[count - 1])
last_list.sort()

print(last_list[0])