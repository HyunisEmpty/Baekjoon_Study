import sys

for _ in range(3):

    sh, sm, ss, eh, em, es = map(int, sys.stdin.readline().split())

    ss += sh * 60 * 60
    ss += sm * 60

    es += eh * 60 * 60
    es += em * 60

    s = (es - ss)%60
    m = ((es - ss)//60)%60
    h = (((es - ss)//60)//60)%60

    print(h, m, s)