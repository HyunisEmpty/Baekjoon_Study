import sys

"""변수설명
n : 1로 만들고자 하는 수 
min_count : 최소 연산 횟수 
count : 현재 연산 횟수 
"""

n = int(sys.stdin.readline().strip())
min_count = n - 1

def GotoOne(number, cnt):

    global min_count

    # number가 목표값 1에 도달한 경우에 최소 연산 초기화후 연산 종료
    if number == 1:
        if min_count > cnt:
            min_count = cnt
        return
    else:

        if cnt > min_count:
            return
        else:
            if number%3 == 0:
                GotoOne(number//3, cnt + 1)
            if number%2 == 0:
                GotoOne(number//2, cnt + 1)
            GotoOne(number - 1, cnt + 1)

GotoOne(n, 0)
print(min_count)