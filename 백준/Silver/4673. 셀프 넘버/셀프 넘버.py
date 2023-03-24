
# 인도 수학자 D.R. Kaprekar가 이름 붙인 셀프 넘버를 구하는 함수
def kaprekar(num):

    all_sum = 0
    original_num = num

    digit_10000 = num // 10000
    num -= digit_10000 * 10000

    digit_1000 = num // 1000
    num -= digit_1000 * 1000

    digit_100 = num // 100
    num -= digit_100 * 100

    digit_10 = num // 10
    num -= digit_10 * 10

    digit_1 = num // 1

    # print(original_num, digit_10000, digit_1000, digit_100, digit_10, digit_1)
    all_sum = original_num + digit_10000 + digit_1000 + digit_100 + digit_10 + digit_1

    return all_sum

number_list = []
for i in range(1, 10001):
    number_list.append(i)

for i in range(10000):
    number = kaprekar(i)
    if number in number_list:
        number_list.remove(number)

for i in number_list:
    print(i)
