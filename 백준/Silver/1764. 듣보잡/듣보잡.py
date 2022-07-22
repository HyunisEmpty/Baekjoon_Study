listen_count, see_count = map(int, input( ).split(" "))

listen_list = []
for count in range(listen_count):
    listen_list.append(input())

see_list = []
for count in range(see_count):
    see_list.append(input())

unknown_list = list(set(listen_list) & set(see_list))

print(len(unknown_list))
unknown_list.sort()
for carrier in unknown_list:
    print(carrier)