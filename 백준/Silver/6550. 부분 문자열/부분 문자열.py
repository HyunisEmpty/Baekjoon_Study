import sys

while True:

    try:
        s, t = map(str, sys.stdin.readline().split())
        index = 0

        # 문자열 t를 한 글자씩 확인
        for t_word in t:

            # 모든 문자가 s안에 들어 있는 경우
            if index == len(s):
                break

            # s의 index번째 단어와 동일한지 확인
            if t_word == s[index]:
                # print(s[index], t_word)
                index += 1

        # print(index, len(s) - 1)
        if index == len(s):
            print("Yes")
        else:
            print("No")
    except:
        break