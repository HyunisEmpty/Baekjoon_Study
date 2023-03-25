import sys


# 종말 수 인지 판단하는 함수
def end_number(num):

    num = str(num)

    for i in range(2,len(num)):
        if num[i] == "6" and num[i-1] == "6" and num[i-2] == "6":
            return True

    return False


n = int(sys.stdin.readline().strip())

count = 0
number = 665
flag = True

# 브루트 포스 알고리즘
while flag:

    number += 1

    if end_number(number):
        count += 1

    if count == n:
        flag = False

print(number)
