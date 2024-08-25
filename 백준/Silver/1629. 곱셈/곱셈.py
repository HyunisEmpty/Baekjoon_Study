import sys

""" 변수 설명 
dividend : 피제수 
exponent : 지수 
divisor : 제수 
"""

dividend, exponent, divisor = map(int, sys.stdin.readline().split())
dividend_2 = 1

while exponent != 1:

    # print(dividend, dividend_2, exponent, divisor)

    # 피제수가 제수 보다 작은 경우 => 피제수를 제수보다 크게 만든다.
    if dividend < divisor:

        # 지수를 2로 나눈 나머지가 있는 경우
        if exponent % 2 == 1:
            # 지수를 2로 나누고 나머지 1만큼 피제수2에 곱한다.
            exponent = exponent // 2
            dividend_2 *= dividend
        # 지수를 2로 나눈 나머지가 있는 경우
        else:
            exponent = exponent // 2

        # 피제수를 제곱한 수를 제수로 나눠 지수를 약절반으로 감소
        dividend = (dividend ** 2) % divisor
        dividend_2 = dividend_2 % divisor

    # 피제수가 제수보다 큰 경우
    elif dividend > divisor:

        # 피제수를 제수보다 크게 만들 필요가 없다.
        dividend = dividend % divisor
        dividend_2 = dividend_2 % divisor

    # 피제수와 제수가 같은 경우 => 연산 종료 0 출력
    else:
        dividend = 1
        break


print((dividend * dividend_2) % divisor)