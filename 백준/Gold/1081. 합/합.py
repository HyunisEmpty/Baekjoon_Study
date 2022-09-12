import sys

# 시작값을 start에 끝값을 stop에 입력받는다.
start, stop = map(str, sys.stdin.readline().split())

if int(start) != 0:
    a = int(start)
    a -= 1
    start = str(a)

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

#각 자리수별 숫자들의 총합을 구하는 함수
def AllSumMaker(target_list):
    # 모든 데이터의 총합을 의미한다.
    all_sum = 0
    index_sum = 0
    for target in target_list:
        index_target = int(target[0])

        # 공식 1구간
        area1_sum = 0
        area1_sum += index_target
        # print("제 1구역 :", area1_sum)

        # 공식 2구간
        area2_sum = 0
        area2_carrier = 0
        for count in range(0, index_target):
            area2_carrier += count
        area2_sum += area2_carrier * (10**(len(target)-1))
        # print("제 2구역 :", area2_sum)

        # 공식 3구간
        area3_sum = 0
        if len(target) == 1:
            area3_sum += 0
        else:
            area3_sum += 45 * (10 ** ((len(target)) - 2)) * (len(target) - 1) * index_target
        # print("제 3구역 :", area3_sum)

        # 공식 4구간
        area4_sum = 0
        area4_sum += index_sum * int(target)
        # print("제 4구역 :", area4_sum)

        # 최종출력을 위한 총합을 구함
        all_sum += area1_sum + area2_sum + area3_sum + area4_sum

        index_sum += index_target
        # print("index_sum :",index_sum)

    return all_sum

start_list = DigitListMaker(start)
stop_list = DigitListMaker(stop)

# print("start : ", DigitListMaker(start))
# print("stop : ", DigitListMaker(stop))

start_all_sum = AllSumMaker(start_list)
stop_all_sum = AllSumMaker(stop_list)

# print("start all sum :", AllSumMaker(start_list))
# print("stop all sum :", AllSumMaker(stop_list))

answer = stop_all_sum - start_all_sum
print(answer)
