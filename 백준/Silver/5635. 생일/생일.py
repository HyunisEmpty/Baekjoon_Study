import sys

n = int(sys.stdin.readline().strip())

birth_day_list = []
birth_day_dic = {}
for i in range(n):
    name, dd, mm, year = map(str, sys.stdin.readline().split())

    if len(dd) < 2:
        dd = "0" + dd

    if len(mm) < 2:
        mm = "0" + mm

    birth_day_list.append(year + mm + dd)
    birth_day_dic[year + mm + dd] = name

birth_day_list.sort()
print(birth_day_dic[birth_day_list[n-1]])
print(birth_day_dic[birth_day_list[0]])
