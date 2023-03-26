import sys
# 길이가 짧은것부터, 길이가 같으면 사전순으로

n = int(sys.stdin.readline().strip())
word_dic = {}
key_list = []

# 문자의 길이를 키, 문자를 값으로 해서 딕셔너리에 저장한다.
for i in range(n):
    word = sys.stdin.readline().strip()

    # 입력된 문자열의 경우가 처음인 경우
    if len(word) not in word_dic.keys():
        word_dic[len(word)] = [word]
        key_list.append(len(word))
    else:
        # 문자 중복 제거를 위해서
        if word not in word_dic[len(word)]:
            word_dic[len(word)].append(word)

# 키값만 있는 리스트를 정렬
for i in range(len(key_list)-1):
    min_index = i
    for j in range(i, len(key_list)):
        if key_list[min_index] > key_list[j]:
            min_index = j
    key_list[min_index], key_list[i] = key_list[i], key_list[min_index]

# key에 해당하는 문자열이 저장된 리스트를 반복문을 통해서 정렬
for key in key_list:
    word_dic[key].sort()

for key in key_list:
    for i in word_dic[key]:
        print(i)
