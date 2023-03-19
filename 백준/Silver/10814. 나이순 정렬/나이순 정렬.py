import sys

n = int(sys.stdin.readline().strip())

customer_dic = {}
age_list = []
for count in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)

    if age not in customer_dic.keys():
        customer_dic[age] = [name]
        age_list.append(age)
    else:
        customer_dic[age].append(name)

# 선택 정렬
for i in range(len(age_list)-1):
    min_index = i
    for j in range(i, len(age_list)):
        if age_list[min_index] > age_list[j]:
            min_index = j
    age_list[min_index], age_list[i] = age_list[i], age_list[min_index]

for age_data in age_list:
    for name_val in customer_dic[age_data]:
        print(str(age_data) + " " + name_val)