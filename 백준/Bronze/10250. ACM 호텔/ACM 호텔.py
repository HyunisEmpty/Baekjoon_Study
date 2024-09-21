import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    h, w, n = map(int, sys.stdin.readline().split())

    # 층수 판별
    y_nh = n%h
    # h//n번 호실 최상층인경우
    if y_nh == 0:
        yy = str(h)
        xx = str(n//h)
    # h//n + 1번 호실 h%n층 인경우
    else:
        yy = str(n%h)
        xx = str(n//h + 1)

    if len(xx) == 1:
        xx = "0" + xx

    print(yy + xx)
