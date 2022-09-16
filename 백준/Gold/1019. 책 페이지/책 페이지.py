import sys

# target_page = input()
target_page = sys.stdin.readline().strip()
page_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index_list = []


# 자리수 별로 분리하는 함수
def DigitListMaker(target_list):
    target_list = target_list[::-1]
    digit_list = []
    for count in range(len(target_list)):
        # 자릿수 별로 구분 하여 리스트에 저장
        if count == 0:
            digit = 1
        else:
            digit = 10 ** (count)
        first_number = int(target_list[count])
        first_number = first_number * (digit)
        digit_list.append(str(first_number))
    digit_list = digit_list[::-1]
    return digit_list
# print(DigitListMaker(target_page))


def ZeroCutter(target_list):
    target_number = target_list[0]


    # 첫번째 대상에 대한 0제거
    cutter_num = 0
    if len(target_number) >= 2:
        for count in range(len(target_number)-1):
            cutter_num += 10 ** count
            
    return cutter_num


#각 자리수별 숫자들의 총합을 구하는 함수
def AllSumMaker(target_list):

    first_number = target_list[0]

    for target in target_list:

        index_target = int(target[0])

        # 공식 1구간
        page_list[index_target] += 1
        # print("1구간 :", page_list)

        # 공식 2구간
        for count in range(0, index_target):
            if target == first_number:
                if count == 0:
                    pass
                else:
                    page_list[count] += 10 ** (len(target) - 1)
            else:
                page_list[count] += 10 ** (len(target) - 1)

        # print("2구간 :", page_list)

        # 공식 3구간
        if len(target) == 1:
            pass
        else:
            # 1~9까지에 대한 연산
            for count in range(0, 10):
                page_list[count] += (10 ** ((len(target)) - 2)) * (len(target) - 1) * index_target


        # print("3구간 :", page_list)

        # 공식 4구간
        for count in index_list:
            page_list[int(count)] += int(target)

        index_list.append(index_target)
        # print(page_list)

    return page_list

cutter_num = ZeroCutter(DigitListMaker(target_page))
answer_list = AllSumMaker(DigitListMaker(target_page))
answer_list_0 = answer_list[0]
answer_list[0] = answer_list_0 - cutter_num
print(*answer_list)