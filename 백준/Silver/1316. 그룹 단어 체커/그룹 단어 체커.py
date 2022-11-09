import sys

test_case = int(sys.stdin.readline().strip())

word_count = 0
# 테스트 케이스 만큼 for문이 동아가도록 설정한다.
for test_count in range(test_case):
    # 개행문자를 제거한 문자열을 입력받는다.
    str = sys.stdin.readline().strip()
    str_bool = True
    str_list = []

    # 문지열의 길이만큼 for문을 돌려 모든 문자에 접근한다.
    for count in range(len(str)):
        # 만약 문자가 문자 리스트에 들어 있다면
        if str[count] in str_list:
            # 현재 문자가 리스트 가장 뒤에 있는지 확인한다.
            if str_list[-1] != str[count]:
                # 만약 리스트의 가장 뒤에 있지 않다면 그룹문자가 아니므로 srt_bool을 False로 바꾸어 word_count가 동작하지 않도록 한다.
                str_bool = False
        # 만약 문자가 문자 리스트에 들어 있지 않다면
        else:
            # 문자 리스트에 현재 문자를 추가 한다.
            str_list.append(str[count])

    if(str_bool):
        # print("word_count 진입")
        word_count += 1

print(word_count)
