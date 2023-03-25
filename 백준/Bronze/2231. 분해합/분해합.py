import sys

# 인도 수학자 D.R. Kaprekar가 이름 붙인 셀프 넘버를 구하는 함수
def kaprekar(num):

    all_sum = 0
    original_num = num

    digit_1000000 = num // 1000000
    num -= digit_1000000 * 1000000

    digit_100000 = num // 100000
    num -= digit_100000 * 100000

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
    all_sum = original_num + digit_1000000 + digit_100000 + digit_10000 + digit_1000 + digit_100 + digit_10 + digit_1

    return all_sum


n = int(sys.stdin.readline().strip())

# 브루트 포스 알고리즘
count = 0
for i in range(1, n + 1):
    number = kaprekar(i)

    if number == n:
        print(i)
        break
    else:
        count += 1

if count == n:
    print(0)