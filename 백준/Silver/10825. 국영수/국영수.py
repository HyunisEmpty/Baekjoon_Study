import sys

n = int(sys.stdin.readline().strip())

korea_dic = dict()
english_dic = dict()
math_dic = dict()
name_dic = dict()
for _ in range(n):

    name, korea_s, english_s, math_s = map(str, sys.stdin.readline().strip().split())

    korea = int(korea_s)
    english = int(english_s)
    math = int(math_s)

    if korea_s + " " + english_s + " " + math_s not in name_dic:
        name_dic[korea_s + " " + english_s + " " + math_s] = [name]
    else:
        name_dic[korea_s + " " + english_s + " " + math_s].append(name)
        name_dic[korea_s + " " + english_s + " " + math_s].sort()

    # 수학 점수를 기준으로 내림차순으로 정렬
    if korea not in korea_dic:  # korea 점수가 처음 입력된 경우
        korea_dic[korea] = [english]
    else:                       # korea 점수가 2번이상 입력된 경우
        korea_dic[korea].append(english)

    if english not in english_dic:
        english_dic[english] = [math]
    else:
        english_dic[english].append(math)

    if math not in math_dic:
        math_dic[math] = [name]
    else:
        math_dic[math].append(name)

for korea_key in sorted(list(set(korea_dic.keys())), reverse=True):

    for english_key in sorted(list(set(korea_dic[korea_key]))):

        for math_key in sorted(list(set(english_dic[english_key])), reverse=True):

            korea_s = str(korea_key)
            english_s = str(english_key)
            math_s = str(math_key)

            if korea_s + " " + english_s + " " + math_s in name_dic:
                for name in name_dic[korea_s + " " + english_s + " " + math_s]:
                    print(name)
